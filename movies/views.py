from msilib.schema import ServiceInstall
from urllib import response
from django.db.models import Count
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from .models import Movie, Genre, Comment
from .serializers.movie import MovieListSerializer
from .serializers.comment import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def movie_list(request, page):

    movies = Movie.objects.annotate(
        comment_count = Count('comments', distinct=True),            # https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
        like_count = Count('like_users', distinct=True)
    ).all()[page:page+100]
    print(movies)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET', 'POST'])
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