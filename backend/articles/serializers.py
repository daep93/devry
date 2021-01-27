from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title','image', 'author')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'article')
        # read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
   
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
        fields = ('id', 'title', 'content', 'author', 'like', 'view', 'image', 'created_at', 'updated_at','comment_set', 'comment_count',)
