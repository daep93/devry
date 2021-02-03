from rest_framework import serializers,fields
from .models import Article, Comment, tech

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
    ref_tags= fields.MultipleChoiceField(choices=tech)
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
        fields = ('id','title', 'content','author','ref_tags', 'like_users', 'liked', 'like_num', 'bookmark_users', 'bookmarked',
        'bookmark_num', 'viewed_num', 'thumbnail_img', 'written_time', 'updated_at','comment_set', 'comment_count',)


class ArticleProfileSerializer(serializers.ModelSerializer):
    ref_tags= fields.MultipleChoiceField(choices=tech)
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )
    class Meta:
        model = Article
        fields = ('id', 'title', 'written_time', 'content', 'thumbnail_img', 'like_num', 'comment_count', 'ref_tags')


class CommentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'article', 'written_time', 'comment_content')


class PinnedPostsProfileSerializer(serializers.ModelSerializer):
    ref_tags= fields.MultipleChoiceField(choices=tech)
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )
    class Meta:
        model = Article
        fields = ('id', 'title', 'written_time', 'content', 'thumbnail_img', 'like_num', 'comment_count', 'ref_tags')


class likeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', "liked")


class bookmarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', "bookmarked")
