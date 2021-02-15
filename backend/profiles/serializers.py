from rest_framework import serializers, fields
from .models import Profile, Link, Projects
from .models import tech, user_tag
from accounts.models import User
from django.shortcuts import get_object_or_404

from accounts.serializers import UserSerializer, UserEmailSerializer, UserFollowerNumberSerializer, UserJoinedSerializer, UserFollowingNumberSerializer


class ProfileLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        # fields = ( 'sns_url1', 'sns_url2', 'sns_url3')
        fields = ('sns_name1', 'sns_url1', 'sns_name2', 'sns_url2', 'sns_name3', 'sns_url3')


class ProfileProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('project_name1', 'project_url1', 'project_name2', 'project_url2', 'project_name3', 'project_url3')

class ProfileTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('tags',)

class ProfilePostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('posts',)

class ProfilePinnedPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('pinned_posts', )

class ProfileCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('comments', )




class ProfileSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    tag = fields.MultipleChoiceField(choices=user_tag)        

    links = ProfileLinkSerializer(many=True, read_only=True)
    projects = ProfileProjectSerializer(many=True, read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    # follower_num = serializers.IntegerField(read_only=True)
    # followee_num = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'email', 'username', 'joined', 'follower_num', 'followee_num', 'profile_img', 'region', 'group', 'bio', 'links', 'sns_name1', 'sns_name2', 'sns_name3', 'sns_url1', 'sns_url2', 'sns_url3',
        'tech_stack', 'projects', 'project_name1', 'project_name2', 'project_name3', 'project_url1', 'project_url2', 'project_url3', 'tag', 'pinned_posts', 'posts', 'comments',  )



class ProfileShowSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)

    link = ProfileLinkSerializer(many=True, read_only=True)
    project = ProfileProjectSerializer(many=True, read_only=True)
    follower_num = serializers.IntegerField(read_only=True)
    followee_num = serializers.IntegerField(read_only=True)


    tags = ProfileTagSerializer(read_only=True)
    posts = ProfilePostsSerializer(many=True, read_only=True)
    pinned_posts = ProfilePinnedPostsSerializer(many=True, read_only=True)
    comments = ProfileCommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'email', 'username', 'joined', 'follower_num', 'followee_num', 'profile_img', 'region', 'group', 'bio', 'link', 
        'tech_stack', 'project', 'tags', 'pinned_posts', 'posts', 'comments',  )


class ProfileListSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    tag = fields.MultipleChoiceField(choices=user_tag)      

    link = ProfileLinkSerializer(many=True, read_only=True)

    project = ProfileProjectSerializer(many=True, read_only=True)


    class Meta:
        model = Profile
        fields = ('email', 'profile_img', 'region', 'group', 'bio', 'link', 'tech_stack', 'project', 'tag', )
        read_only_fields = ('profile_img', 'link', 'project')
 


class ProfileUpdateSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    tag = fields.MultipleChoiceField(choices=user_tag)

    # links = ProfileLinkSerializer(many=True, read_only=True)
    links = fields.ListField()
    projects = fields.ListField()
    class Meta:
        model = Profile
        fields = ( 'username', 'profile_img', 'region', 'group', 'bio', 'links', 'tech_stack', 'projects', 'tag',
        'sns_name1', 'sns_name2', 'sns_name3', 'sns_url1', 'sns_url2', 'sns_url3', 'project_name1', 'project_name2', 'project_name3', 'project_url1', 'project_url2', 'project_url3')
        extra_kwargs = {
            'sns_name1': {"write_only": True},
            'sns_name2': {"write_only": True}, 
            'sns_name3': {"write_only": True}, 
            'sns_url1': {"write_only": True},
            'sns_url2': {"write_only": True},
            'sns_url3': {"write_only": True},  
            'project_name1': {"write_only": True},
            'project_name2': {"write_only": True}, 
            'project_name3': {"write_only": True}, 
            'project_url1': {"write_only": True},
            'project_url2': {"write_only": True},
            'project_url3': {"write_only": True},  

        }


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.profile_img = validated_data.get('profile_img', instance.profile_img)
        instance.region = validated_data.get('region', instance.region)
        instance.group = validated_data.get('group', instance.group)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.links = validated_data.get('links', instance.links)
        instance.tech_stack = validated_data.get('tech_stack', instance.tech_stack)
        instance.projects = validated_data.get('projects', instance.projects)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.sns_name1 = validated_data.get('sns_name1', instance.sns_name1)
        instance.sns_url1 = validated_data.get('sns_url1', instance.sns_url1)
        instance.sns_name2 = validated_data.get('sns_name2', instance.sns_name2)
        instance.sns_url2 = validated_data.get('sns_url2', instance.sns_url2)
        instance.sns_name3 = validated_data.get('sns_name3', instance.sns_name3)
        instance.sns_url3 = validated_data.get('sns_url3', instance.sns_url3)
        instance.project_name1 = validated_data.get('project_name1', instance.project_name1)
        instance.project_url1 = validated_data.get('project_url1', instance.project_url1)
        instance.project_name2 = validated_data.get('project_name2', instance.project_name2)
        instance.project_url2 = validated_data.get('project_url2', instance.project_url2)
        instance.project_name3 = validated_data.get('project_name3', instance.project_name3)
        instance.project_url3 = validated_data.get('project_url3', instance.project_url3)
        instance.save()
        return instance

class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'profile_img')