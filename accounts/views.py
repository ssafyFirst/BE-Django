from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import ProfileSerializer, CustomRegisterSerializer
from rest_framework.response import Response

# Create your views here.

User = get_user_model()


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['PUT'])
def update(request, username):
    user = get_object_or_404(User, username=username)
    if user == request.user:
        serializer = CustomRegisterSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
