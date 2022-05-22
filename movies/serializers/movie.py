from rest_framework import serializers
from django.contrib.auth import get_user_model


from ..models import Movie

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    
    comment_count = serializers.IntegerField(read_only=True)
    like_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_path', 'comment_count', 'like_count')