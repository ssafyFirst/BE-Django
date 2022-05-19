from django.db.models import Count

from rest_framework.response import Response
from .models import Movie, Genre, Comment
from .serializers.movie import MovieListSerializer
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def movie_list(request):
    movies = Movie.objects.annotate(
        comment_count = Count('comments', distinct=True),            # https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
        like_count = Count('like_users', distinct=True)
    )
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    