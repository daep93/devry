from rest_framework import serializers, fields
from .models import Profile
# from .models import Profile, Link, Project
from .models import tech, user_tag
from accounts.models import User
from django.shortcuts import get_object_or_404

from articles.serializers import ArticleProfileSerializer, ArticleListSerializer, ArticleSerializer, CommentProfileSerializer, PinnedPostsProfileSerializer
from accounts.serializers import UserSerializer, UserEmailSerializer, UserFollowerNumberSerializer, UserJoinedSerializer


class ProfileLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('sns_name1', 'sns_name2', 'sns_name3', 'sns_url1', 'sns_url2', 'sns_url3',)

class ProfileProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('project_name1', 'project_name2', 'project_name3', 'project_url1', 'project_url2', 'project_url3')

class ProfileTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('tags',)


class ProfileLinkUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', )

class ProfileSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    tag = fields.MultipleChoiceField(choices=user_tag)        

    links = ProfileLinkSerializer(many=True, read_only=True)
    projects = ProfileProjectSerializer(many=True, read_only=True)
    # joined = UserJoinedSerializer(read_only=True)
    follower_num = serializers.IntegerField(read_only=True)
    followee_num = serializers.IntegerField(read_only=True)
    # email = UserEmailSerializer(read_only=True)
    posts = ArticleProfileSerializer(many=True, read_only=True)
    # posts = ArticleProfileSerializer(read_only=True)
    comments = CommentProfileSerializer(many=True, read_only=True)
    # comments = CommentProfileSerializer(read_only=True)
    pinned_posts = PinnedPostsProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'email', 'username', 'joined', 'follower_num', 'followee_num', 'profile_img', 'region', 'group', 'bio', 'links', 'sns_name1', 'sns_name2', 'sns_name3', 'sns_url1', 'sns_url2', 'sns_url3',
        'tech_stack', 'projects', 'project_name1', 'project_name2', 'project_name3', 'project_url1', 'project_url2', 'project_url3', 'tag', 'pinned_posts', 'posts', 'comments',  )

class ProfileShowSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    # tag = fields.MultipleChoiceField(choices=user_tag)        

    links = ProfileLinkSerializer(many=True, read_only=True)
    projects = ProfileProjectSerializer(many=True, read_only=True)

    # joined = UserJoinedSerializer(read_only=True)
    # joined = serializers.DateTimeField()
    tags = ProfileTagSerializer()
    # follow_count = UserFollowerNumberSerializer(read_only=True)
    # email = UserEmailSerializer(read_only=True)
    posts = ArticleProfileSerializer(many=True, read_only=True)
    # posts = ArticleProfileSerializer(read_only=True)
    comments = CommentProfileSerializer(many=True, read_only=True)
    # comments = CommentProfileSerializer(read_only=True)
    pinned_posts = PinnedPostsProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'email', 'username', 'joined', 'follower_num', 'followee_num', 'profile_img', 'region', 'group', 'bio', 'links', 
        'tech_stack', 'projects', 'tags', 'pinned_posts', 'posts', 'comments',  )

class ProfileListSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    tag = fields.MultipleChoiceField(choices=user_tag)      
    # email = UserEmailSerializer(read_only=True)

    links = ProfileLinkSerializer(many=True, read_only=True)
    projects = ProfileProjectSerializer(many=True, read_only=True)

    
    class Meta:
        model = Profile
        fields = ('user', 'email', 'profile_img', 'region', 'group', 'bio', 'links', 'tech_stack', 'projects', 'tag',)
 
 
class ProfileUpdateSerializer(serializers.ModelSerializer):
    tech_stack = fields.MultipleChoiceField(choices=tech)
    tag = fields.MultipleChoiceField(choices=user_tag)

    links = ProfileLinkSerializer(many=True, read_only=True)
    # links_edit = ProfileLinkSerializer(many=True, read_only=True)
    projects = ProfileProjectSerializer(many=True, read_only=True)
    # projects_edit = ProfileProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', 'region', 'group', 'bio', 'links', 'tech_stack', 'projects', 'tag')


class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'profile_img')