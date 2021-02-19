from rest_framework import serializers, fields
from .models import Event, tech
from profiles.models import Profile
from accounts.models import User


class UserinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class EventMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'thumnail')


class EventListSerializer(serializers.ModelSerializer):
    
    user = UserinfoSerializer(
        read_only=True,
    )

    class Meta:
        model = Event
        fields = ('id', 'thumnail', 'category', 'title', 'ref_tags', 'start', 'end', 'host_name', 'profile_img', 'bookmarked', 'viewed_num', 'bookmark_num', 'user')


class EventdetailSerializer(serializers.ModelSerializer):
    
    ref_tags = fields.MultipleChoiceField(choices=tech)
    
    user = UserinfoSerializer(
        read_only=True,
    )
    
    class Meta:
        model = Event
        fields = ('id', 'state', 'thumnail', 'title', 'category', 'place', 'start', 'end', 'start', 'end', 'cost', 'participation', 'introduction', 'schedule',
        'host_name', 'profile_img', 'register_url', 'ref_tags', 'bookmarked', 'bookmark_num', 'viewed_num', 'user', 'king')


class EventSerializer(serializers.ModelSerializer):

    ref_tags = fields.MultipleChoiceField(choices=tech)
    
    class Meta:
        model = Event
        fields = ('id', 'state', 'thumnail', 'title', 'category', 'place', 'start', 'end', 'cost', 'participation', 'introduction', 'schedule',
       'host_name', 'profile_img', 'register_url', 'ref_tags', 'bookmarked', 'bookmark_num', 'viewed_num', 'user', 'king')


class bookmarkSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Event
        fields = ('id', "bookmarked")


class mybookmarkSerializer(serializers.ModelSerializer):
         
    user = UserinfoSerializer(
        read_only=True,
    )

    class Meta:
        model = Event
        fields = ('id', 'thumnail', 'category', 'title', 'ref_tags', 'start', 'end', 'host_name', 'profile_img', 'bookmarked', 'viewed_num', 'bookmark_num', 'user')
