from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from movies.models import Movie
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    profile_img = serializers.ImageField(use_url=True, required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_img'] = self.validated_data.get('profile_img', '')
        # data['like_genres'] = self.validated_data.get('like_genrses', [])
        
        return data


class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'title',)
    
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'profile_img', 'like_movies',)