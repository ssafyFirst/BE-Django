from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Genre


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'