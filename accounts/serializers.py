from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from movies.models import Movie, Genre
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    class LikeGernesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('pk',)
    like_gernes = LikeGernesSerializer(many=True, read_only=True)
    
    profile_img = serializers.ImageField(use_url=True, required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_img'] = self.validated_data.get('profile_img', '')
        
        return data


class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'title')
    
    like_movies = MovieSerializer(many=True)
    movie = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'like_movies', 'movie',)