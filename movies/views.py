from django.db.models import Count
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from accounts.serializers import ProfileSerializer
from actors.models import Actor
from actors.serializers import ActorSerializer
from .models import Movie, Comment, Genre
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.comment import CommentSerializer
from .serializers.genre import GenreListSerializer, GenreNameListSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

@api_view(['GET', 'POST'])
def movie_list(request, page):

    movies = Movie.objects.annotate(
        comment_count = Count('comments', distinct=True),            # https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
        like_count = Count('like_users', distinct=True)
    ).all()[page:page+100]
    print(movies)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    

@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = movie.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
    
    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = movie.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        
        serializer = MovieSerializer(movie)
        
        return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        comments = movie.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)

    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def genres_list(request):
    genres = Genre.objects.all()
    serializer = GenreNameListSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recommendation(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)