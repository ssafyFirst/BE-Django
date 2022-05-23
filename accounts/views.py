from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import ProfileSerializer
from rest_framework.response import Response
# Create your views here.

User = get_user_model()

def signup2(request):
    print(request)

api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializers = ProfileSerializer(user)
    return Response(serializers.data)