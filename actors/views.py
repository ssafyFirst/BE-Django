from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ActorListSerializer
from .models import Actor
# Create your views here.

@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)