from rest_framework import serializers, fields
from .models import Post, Comment, tech
from profiles.models import Profile
from profiles.serializers import ProfileSerializer, ProfileListSerializer
from accounts.models import User


class UserinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 'id', 'username')


class ProfilepostListSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', )


class ProfilepostSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', 'follower_num', 'bio')
# 부족한 필드 추가해야함


class WriterInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('user', )


class ProfilePostSerializer(serializers.ModelSerializer):
    
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
        )

    class Meta:
        model = Post
        fields = ('id', 'title', 'username', 'written_time', 'thumbnail', 'like_num', 'comment_count', 'ref_tags',)


class PostListforamtSerializer(serializers.ModelSerializer):
    
    user = UserinfoSerializer(
        read_only=True,
    )

    profile = ProfilepostListSerializer(
        read_only=True,
    )
    
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'title','user', 'written_time', 'ref_tags', 'like_num', 'comment_count', 'viewed_num', 'liked', 'profile')


class PostListSerializer(serializers.ModelSerializer):
    
    profile = ProfilepostListSerializer(
        read_only=True,
    )
    
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'written_time', 'ref_tags', 'like_num', 'comment_count', 'viewed_num', 'liked', 'profile')


class CommentdetailSerializer(serializers.ModelSerializer):

    profile = ProfilepostListSerializer(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'user','like_comment_num', 'post', 'written_time', 'liked_comment' ,'profile')

 
class CommentlistSerializer(serializers.ModelSerializer):
    
    profile = ProfileListSerializer(
        read_only=True
    )

    user = UserinfoSerializer(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'like_comment_num', 'user', 'post', 'written_time', 'liked_comment' ,'profile')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',  'comment_content', 'like_comment_num', 'user', 'post', 'written_time', 'liked_comment', 'profile')

class PostSerializer(serializers.ModelSerializer):

    ref_tags= fields.MultipleChoiceField(choices=tech)

    comment_set = CommentSerializer(
        many=True,
        read_only=True,   
    )

    comment_num = serializers.IntegerField(
        source='comment_set.num',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id','user', 'title','content','ref_tags', 'bookmark_num', 'bookmarked', 'like_num', 'liked',
        'viewed_num', 'comment_num', 'written_time','comment_set', )

class PostdetailSerializer(serializers.ModelSerializer):

    # ref_tags= fields.MultipleChoiceField(choices=tech)
    
    # user = UserinfoSerializer(
    #     read_only=True,
    # )

    writer_info = ProfilepostSerializer(
        many=True,
        read_only=True,
    )

    forum_post = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'writer_info', 'forum_post')
        # fields = ('id','writer_info', 'title','written_time', 'ref_tags', 'like_num', 'comment_count',
        # 'viewed_num', 'bookmark_num','content', 'comment_set', 'liked', 'bookmarked','user' )




class likeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', "liked")


class like_commentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', "liked_comment")


class bookmarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', "bookmarked")
