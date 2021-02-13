from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostListSerializer, ProfilepostSerializer, PostListforamtSerializer, PostSerializer,CommentSerializer, likeSerializer, bookmarkSerializer, like_commentSerializer, UserinfoSerializer,ProfileListSerializer ,PostdetailSerializer,CommentlistSerializer,CommentdetailSerializer
from .models import Post, Comment
from rest_framework import viewsets
from profiles.models import Profile
from accounts.models import User

from mysite.utils import jwt_encode
from rest_auth.models import TokenModel
from rest_framework.authtoken.models import Token
from mysite.app_settings import TokenSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
def post_list(request):
    """
    Post 글 목록 보기

    ---
    """
    if request.method == 'GET':
        # 토큰을 이용한 사용자 획인 코드
        if request.META.get('HTTP_AUTHORIZATION'):           
            tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
            user=User.objects.get(id=tok.user_id)
            request.user = user
       
        posts = Post.objects.all() 
        for post in posts:
            post.like_num = post.like_users.count() 
            if post.like_users.filter(id=request.user.pk).exists():
                post.liked = "True"      
            else:
                post.liked = "False"
            post.save()  
        # post number in user_id -> It will be "True"
        serializer = PostListforamtSerializer(posts, many=True)
        return Response(serializer.data) 


@api_view(['GET', 'POST'])
def post_list_create(request):
    """
    Post 글 작성

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        posts = Post.objects.all()
        for post in posts:
            post.like_num = post.like_users.count() 
            if post.like_users.filter(id=request.user.pk).exists():
                post.liked = "True"      
            else:
                post.liked = "False"
            post.save()
            # post number in user_id -> It will be "True"
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data) 
    else:
        profiles = Profile.objects.all()
        if profiles.filter(user_id=request.user.id).exists():
            pro=profiles.get(user_id=request.user.id)
            request.data['profile'] = pro.id

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()     
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_update_delete(request, post_pk):
    """
    Post 글 상세보기,수정,삭제

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    post = get_object_or_404(Post, pk=post_pk)
    post.like_num = post.like_users.count()  # like_num check
    post.bookmark_num = post.bookmark_users.count()  # bookmark_num check
    post.viewed_num = post.viewed_num + 1 # viewed_num++
    post.save()
    # like_check
    comments = Comment.objects.all()
    for comment in comments:
        comment.like_comment_num = comment.like_comment_users.count()
        if comment.like_comment_users.filter(id=request.user.pk).exists():
            comment.liked_comment = "True"      
        else:
            comment.liked_comment = "False"
        comment.save()

    if post.like_users.filter(pk=request.user.pk).exists():
        post.liked="True"
    else:
        post.liked="False"
    # bookmark_check
    if post.bookmark_users.filter(pk=request.user.pk).exists():
        post.bookmarked="True"
    else:
        post.bookmarked="False"
       
    if request.method == 'GET':
        serializer = PostdetailSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        post.delete()
        return Response({ 'id': post_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def create_comment(request, post_pk):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    post = get_object_or_404(Post, pk=post_pk)
    serializer = commentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def comment_list(request):
    """
    큰댓글(답변) 목록 불러오기 및 큰 댓글 작성

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        comments = Comment.objects.all()
        for comment in comments:
            comment.like_comment_num = comment.like_comment_users.count()
            if comment.like_comment_users.filter(id=request.user.pk).exists():
                comment.liked_comment = "True"      
            else:
                comment.liked_comment = "False"
            comment.save()
        comments = Comment.objects.all()
        serializer = CommentlistSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        profiles = Profile.objects.all()
        if profiles.filter(user_id=request.user.id).exists():
            pro=profiles.get(user_id=request.user.id)
            request.data['profile'] = pro.id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()     
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, comment_pk):
    """
    comment  상세보기,수정,삭제

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        comment.like_comment_num = comment.like_comment_users.count()
        if comment.like_comment_users.filter(id=request.user.pk).exists():
            comment.liked_comment = "True"      
        else:
            comment.liked_comment = "False"
        comment.save()
        serializer = CommentdetailSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentdetailSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def like(request, post_pk):
    """
    Post 글 좋아요

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    # user authentication process
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        if post.like_users.filter(pk=request.user.pk).exists():
            post.liked="True"
            serializer = likeSerializer(post)
        else:
            post.liked="False"
            serializer = likeSerializer(post)
        return Response(serializer.data)

        # user가 post 좋아요 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if post.like_users.filter(pk=request.user.pk).exists():
            # like canceled
            post.like_users.remove(request.user)
            return Response("like canceled")
        else:
            # like 
            post.like_users.add(request.user)
            return Response("like !!!!!!")


@api_view(['GET','POST'])
def like_comment(request, comment_pk):
    """
    comment 댓글 좋아요

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    # user authentication process
    # if request.user.is_authenticated:
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        if comment.like_comment_users.filter(pk=request.user.pk).exists():
            comment.liked_comment="True"
            serializer = like_commentSerializer(comment)
        else:
            comment.liked_comment="False"
            serializer = like_commentSerializer(comment)
        return Response(serializer.data)

        # user가 comment 좋아요 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if comment.like_comment_users.filter(pk=request.user.pk).exists():
            # like canceled
            comment.like_comment_users.remove(request.user)
            return Response("comment_like canceled")
        else:
            # like 
            comment.like_comment_users.add(request.user)
            return Response("comment_like !!!!!!")


@api_view(['GET','POST'])
def bookmark(request, post_pk):
    """
    post 북마크 기능

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        if post.bookmark_users.filter(pk=request.user.pk).exists():
            post.bookmarked="True"
            serializer = bookmarkSerializer(post)
        else:
            post.bookmarked="False"
            serializer = bookmarkSerializer(post)
        return Response(serializer.data)

        # user가 post을 북마크 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if post.bookmark_users.filter(pk=request.user.pk).exists():
            # bookmark cancled
            post.bookmark_users.remove(request.user)
            return Response("bookmark cancled")
        else:
            # bookmark
            post.bookmark_users.add(request.user)
            return Response("bookmark")


@api_view(['GET'])
def forum_mybookmark(request):
    """
    my bookmark 목록 불러오기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user

    if request.method == 'GET':
        mark=[]
        posts = Post.objects.all()
        for post in posts:
            if post.bookmark_users.filter(id=request.user.pk).exists():
                mark.append(post)
        
        serializer = PostListforamtSerializer(mark, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def forum_mypost(request):
    """
    내가 작성한 forum 작성 글 목록 불러오기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user

    if request.method == 'GET':
        post = Post.objects.filter(user_id=request.user.pk)
        serializer = PostListforamtSerializer(post, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def forum_mycomment(request):
    """
    내가 작성한 forum 댓글 목록 불러오기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user

    if request.method == 'GET':
        comment = Comment.objects.filter(user_id=request.user.pk)
        serializer = CommentlistSerializer(comment, many=True)
        return Response(serializer.data)
