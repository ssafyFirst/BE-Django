from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from ..models import Comment

User = get_user_model()

class CommentSerializer(ModelSerializer):

    class UserSerializer(ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_img')

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'movie', 'updated_at')
        read_only_fields = ('movie','user',)