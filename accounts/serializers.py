from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from movies.models import Movie, Comment
from django.contrib.auth import get_user_model
from movies.serializers.genre import GenreListSerializer, GenreNameListSerializer

class CustomRegisterSerializer(RegisterSerializer):
    profile_img = serializers.ImageField(use_url=True, required=False, default='profile_img/비로그인.png')
    like_genres = GenreListSerializer(many=True)


    def to_internal_value(self, data):
        print(data.get('like_genres'))
        dicdic = {
            'username': data.get('username'),
            'password1': data.get('password1'),
            'password2': data.get('password2'),
            'profile_img': data.get('profile_img', ''),
            'like_genres': list(map(int, data.get('like_genres').split(',')))
        }
        return dicdic


    def get_cleaned_data(self):
        data = super().get_cleaned_data()

        data['profile_img'] = self.validated_data.get('profile_img', '')
        data['like_genres'] = self.validated_data.get('like_genres', [])
        
        return data


class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'title', 'genres', 'poster_path')
    
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
    
    comments = CommentSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    like_genres = GenreNameListSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'profile_img', 'like_movies', 'comments', 'like_genres')