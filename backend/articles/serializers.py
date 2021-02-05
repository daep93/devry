from rest_framework import serializers,fields
from .models import Article, Comment, tech, tags
from accounts.models import User

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
   
        fields = ('id', 'title','thumbnail_img', 'viewed_num', 'written_time','author','bookmarked','bookmark_num','liked','like_num')
   

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'user', 'profile_img','article' ,'written_time')
        # read_only_fields = ('article',)

        
class ArticleSerializer(serializers.ModelSerializer):
    # ref_tags= fields.MultipleChoiceField(choices=tags)
    comment_set = CommentSerializer(
        many=True,
        read_only=True,
    )

    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )
    
    class Meta:
        model = Article
        fields = ('id','title', 'content','author','tags', 'like_users', 'liked', 'like_num', 'bookmark_users', 'bookmarked',
        'bookmark_num', 'viewed_num', 'thumbnail_img', 'written_time', 'updated_at','comment_set', 'comment_count',)


class ArticleProfileSerializer(serializers.ModelSerializer):
    tags= fields.MultipleChoiceField(choices=tech)
    comment_num = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )
    class Meta:
        model = Article
        fields = ('id', 'title', 'written_time', 'content', 'thumbnail_img', 'like_num', 'comment_num', 'tags')

class CommentProfileTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title',)


class CommentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class CommentProfileSerializer(serializers.ModelSerializer):
    title = CommentProfileTitleSerializer(read_only=True)
    username = CommentUserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'article', 'title', 'username', 'written_time', 'comment_content')



class PinnedPostsProfileSerializer(serializers.ModelSerializer):
    tags= fields.MultipleChoiceField(choices=tech)
    comment_num = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )
    class Meta:
        model = Article
        fields = ('id', 'title', 'written_time', 'content', 'thumbnail_img', 'like_num', 'comment_num', 'tags')


class PinnedUsersProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('pinned_users', )

class likeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', "liked")


class bookmarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', "bookmarked")


class PinnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'pinned_post')