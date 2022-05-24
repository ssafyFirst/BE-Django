from cmath import acos
from rest_framework import serializers
from actors.models import Actor

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name')