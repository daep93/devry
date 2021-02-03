from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, likeSerializer, bookmarkSerializer
from .models import Article, Comment
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()

        for article in articles:
            article.like_num = article.like_users.count()
            article.bookmark_num = article.bookmark_users.count()  
            if article.like_users.filter(id=request.user.pk).exists():
                article.liked = "True"      
            else:
                article.liked = "False"

            if article.bookmark_users.filter(id=request.user.pk).exists():
                article.bookmarked = "True"
            else:
                article.bookmarked = "False"
            article.save()  
            # article number in user_id -> It will be "True"

        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data) 
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.like_num = article.like_users.count()  # like_num check
    article.bookmarked_num = article.like_users.count()  # bookmark_num check
    article.viewed_num = article.viewed_num + 1 # viewed_num++
    article.save()
    # like_check
    if article.like_users.filter(pk=request.user.pk).exists():
        article.liked="True"
    else:
        article.liked="False"
    # bookmark_check
    if article.bookmark_users.filter(pk=request.user.pk).exists():
            article.bookmarked="True"
    else:
        article.bookmarked="False"
       
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        article.delete()
        return Response({ 'id': article_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def like(request, article_pk):
    # user authentication process
    # if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.method == 'GET':
            if article.like_users.filter(pk=request.user.pk).exists():
                article.liked="True"
                serializer = likeSerializer(article)
            else:
                article.liked="False"
                serializer = likeSerializer(article)
            return Response(serializer.data)

        # user가 article을 좋아요 누른 전체유저에 존재하는지.
        if request.method == 'POST':
            if article.like_users.filter(pk=request.user.pk).exists():
                # like canceled
                article.like_users.remove(request.user)
                return Response("like canceled")
            else:
                # like 
                article.like_users.add(request.user)
                return Response("like !!!!!!")


@api_view(['GET','POST'])
def bookmark(request, article_pk):
    # user authentication process
    # if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.method == 'GET':
            if article.bookmark_users.filter(pk=request.user.pk).exists():
                article.bookmarked="True"
                serializer = bookmarkSerializer(article)
            else:
                article.bookmarked="False"
                serializer = bookmarkSerializer(article)
            return Response(serializer.data)

        # user가 article을 북마크 누른 전체유저에 존재하는지.
        if request.method == 'POST':
            if article.bookmark_users.filter(pk=request.user.pk).exists():
                # bookmark cancled
                article.bookmark_users.remove(request.user)
                return Response("bookmark cancled")
            else:
                # bookmark
                article.bookmark_users.add(request.user)
                return Response("bookmark")