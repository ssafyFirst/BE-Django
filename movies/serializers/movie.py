from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.serializers.comment import CommentSerializer
from actors.serializers import ActorSerializer

from actors.models import Actor
from ..models import Movie

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    
    comment_count = serializers.IntegerField(read_only=True)
    like_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_path', 'comment_count', 'like_count')


# 단일 영화
class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    comments = CommentSerializer(many=True, read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    
   

    class Meta:
        model = Movie
        fields = '__all__'