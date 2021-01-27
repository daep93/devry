from rest_framework import serializers
from .models import Event


class EventListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('id', 'title', 'image', 'sdata', 'stime', 'edata', 'etime', 'author')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title','author', 'image', 'like', 'view', 'sdata', 'stime', 'edata', 'etime', 'location', 'cost',
        'target','introduction','schedule','hostinfo','tag','created_at','updated_at')

 