import requests
import json
from datetime import datetime, date, timedelta
import time
import os
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImagePostSerializer, bookmarkSerializer, pinnedSerializer,  pinnedDetailSerializer, ForumpinnedSerializer,\
    ProfilepostListSerializer, ProfilepostSerializer, PostListforamtSerializer, PostListSerializer, \
    CommentdetailSerializer, CommentlistSerializer, CommentSerializer, DetailCommentSerializer, PostSerializer, \
    ForumPostSerializer, PostdetailSerializer, likeSerializer, like_commentSerializer, isfollowingcommentSerializer, \
    isfollowingSerializer

from accounts.serializers import UserFollowingSerializer
from .models import Post, Comment
from rest_framework import viewsets
from profiles.models import Profile
from profiles.serializers import ProfileSerializer, ProfilePostNumberSerializer
from accounts.models import User, Mentioned, UserFollowing
from accounts.serializers import UserSerializer
from qnas.models import Qna
from qnas.serializers import QnapinnedSerializer, QnaDetailPinnedSerializer
from mysite.utils import jwt_encode
from rest_auth.models import TokenModel
from rest_framework.authtoken.models import Token
from mysite.app_settings import TokenSerializer
from PIL import Image, ImageFilter


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
    피드를 통해 사용자가 팔로잉하고 있는 사용자의 일주일 이내 정보를 제공합니다.

    ---
    """

    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
    if request.method == 'GET':
        print(request.user)
        posts = Post.objects.all().order_by('-written_time')   # 최신 순으로 정렬
        following_users = []
        # 사용자의 유저 정보에 팔로잉이 있는 경우 = API로 확인이 가능한 경우
        if request.user != 'AnonymousUser':
            if len(UserSerializer(request.user).data['following']):
                for i in UserSerializer(request.user).data['following']:
                    if i['following_user'] not in following_users:
                        following_users.append(i['following_user'])
        real_posts = Post.objects.filter(user__in=following_users, written_time__gte=datetime.now(
        )-timedelta(days=7))  # 팔로우한 유저이면서 7일 이내의 게시글만 불러오기
        for post in real_posts:
            post.like_num = post.like_users.count()
            if post.like_users.filter(id=request.user.pk).exists():
                post.liked = "True"
            else:
                post.liked = "False"
            post.save()
        serializer = PostListforamtSerializer(real_posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_list_no(request):
    """
    post 제일최신 글 목록 보기

    ---
    """
    if request.method == 'GET':
        # 토큰을 이용한 사용자 획인 코드
        if request.META.get('HTTP_AUTHORIZATION'):
            tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
            user = User.objects.get(id=tok.user_id)
            request.user = user

        posts = Post.objects.all().order_by('-written_time')
        for post in posts:
            post.like_num = post.like_users.count()
            if post.like_users.filter(id=request.user.pk).exists():
                post.liked = "True"
            else:
                post.liked = "False"
            post.ref_tags = list(post.ref_tags)
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
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
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
        serializer = PostListforamtSerializer(posts, many=True)
        return Response(serializer.data)

    else:
        profiles = Profile.objects.all()
        if profiles.filter(user_id=request.user.id).exists():
            pro = profiles.get(user_id=request.user.id)
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
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
    post = get_object_or_404(Post, pk=post_pk)
    post.like_num = post.like_users.count()  # like_num check
    post.bookmark_num = post.bookmark_users.count()  # bookmark_num check
    post.viewed_num = post.viewed_num + 1  # viewed_num++
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
        post.liked = "True"
    else:
        post.liked = "False"
    # bookmark_check
    if post.bookmark_users.filter(pk=request.user.pk).exists():
        post.bookmarked = "True"
    else:
        post.bookmarked = "False"

    if UserFollowing.objects.filter(following_user=post.user, user=request.user.pk).exists():
        post.is_following = "True"
    else:
        post.is_following = "False"

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
        return Response({'id': post_pk}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def create_comment(request, post_pk):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
    post = get_object_or_404(Post, pk=post_pk)
    serializer = commentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def comment_list(request):
    """
    큰댓글(답변) 목록 불러오기 및 큰 댓글 작성

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
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
            pro = profiles.get(user_id=request.user.id)
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
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
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
        return Response({'id': comment_pk}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def like(request, post_pk):
    """
    Post 글 좋아요

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
    # user authentication process
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        serializer = likeSerializer(post)
        if post.like_users.filter(pk=request.user.pk).exists():
            post.liked = "True"
            post.save()
        else:
            post.liked = "False"
            post.save()
        return Response(serializer.data)

        # user가 post 좋아요 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if post.like_users.filter(pk=request.user.pk).exists():
            # like canceled
            post.like_users.remove(request.user)
            post.like_num -= 1
            post.save()
            return Response("like canceled")
        else:
            # like
            post.like_users.add(request.user)
            post.like_num += 1
            post.save()
            return Response("like !!!!!!")


@api_view(['GET', 'POST'])
def like_comment(request, comment_pk):
    """
    comment 댓글 좋아요

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
    # user authentication process
    # if request.user.is_authenticated:
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = like_commentSerializer(comment)
        if comment.like_comment_users.filter(pk=request.user.pk).exists():
            comment.liked_comment = "True"
            comment.save()
        else:
            comment.liked_comment = "False"
            comment.save()
        return Response(serializer.data)

        # user가 comment 좋아요 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if comment.like_comment_users.filter(pk=request.user.pk).exists():
            # like canceled
            comment.like_comment_users.remove(request.user)
            comment.like_comment_num -= 1
            comment.save()
            return Response("comment_like canceled")
        else:
            # like
            comment.like_comment_users.add(request.user)
            comment.like_comment_num += 1
            comment.save()
            return Response("comment_like !!!!!!")


@api_view(['GET', 'POST'])
def bookmark(request, post_pk):
    """
    post 북마크 기능

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        serializer = bookmarkSerializer(post)
        if post.bookmark_users.filter(pk=request.user.pk).exists():
            post.bookmarked = "True"
            post.save()
        else:
            post.bookmarked = "False"
            post.save()
        return Response(serializer.data)

        # user가 post을 북마크 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if post.bookmark_users.filter(pk=request.user.pk).exists():
            # bookmark cancled
            post.bookmark_users.remove(request.user)
            post.bookmark_num -= 1
            post.save()
            return Response("bookmark cancled")
        else:
            # bookmark
            post.bookmark_users.add(request.user)
            post.bookmark_num += 1
            post.save()
            return Response("bookmark")


@api_view(['GET', 'POST'])
def pinned(request, post_pk):
    """
    post pinned 기능

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        serializer = pinnedSerializer(post)
        if post.pinned_users.filter(pk=request.user.pk).exists():
            post.pinneded = "True"
            post.save()
        else:
            post.pinneded = "False"
            post.save()
        return Response(serializer.data)

        # user가 post을 pinned한 전체유저에 존재하는지.
    if request.method == 'POST':
        if post.pinned_users.filter(pk=request.user.pk).exists():
            # pinned cancled
            post.pinned_users.remove(request.user)
            post.pinned_num -= 1
            post.save()
            return Response("pinned cancled")
        else:
            # pinned
            post.pinned_users.add(request.user)
            post.pinned_num += 1
            post.save()
            return Response("pinned")


@api_view(['GET'])
def forum_mybookmark(request):
    """
    my bookmark 목록 불러오기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user

    if request.method == 'GET':
        mark = []
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
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
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
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user

    if request.method == 'GET':
        comment = Comment.objects.filter(user_id=request.user.pk)
        serializer = CommentlistSerializer(comment, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def is_following(request, post_pk):
    """
    forum 글 작성자 팔로잉 여부확인과 팔로잉 하기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
    # user authentication process
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        if UserFollowing.objects.filter(following_user=post.user, user=request.user.pk).exists():
            post.is_following = "True"
            serializer = isfollowingSerializer(post)
        else:
            post.is_following = "False"
            serializer = isfollowingSerializer(post)
        return Response(serializer.data)

    if request.method == 'POST':
        if UserFollowing.objects.filter(following_user=post.user, user=request.user.pk).exists():
            # following canceled
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=post.user_id)
            followee_people.followee_num -= 1
            following_people.follower_num -= 1
            followee_people.save()
            following_people.save()
            UserFollowing.objects.filter(user_id=request.user.pk).delete()
            return Response("following canceled")
        else:
            # following
            serializer = UserFollowingSerializer(data=request.data)
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=post.user_id)
            user = request.user.pk
            following_user = post.user_id
            a = {"user": user, "following_user": following_user}
            serializer = UserFollowingSerializer(data=a)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            followee_people.followee_num += 1
            following_people.follower_num += 1
            followee_people.save()
            following_people.save()
            return Response("following ")


@api_view(['GET', 'POST'])
def is_following_comment(request, comment_pk):
    """
    Ans(큰 댓글) 작성자 팔로잉 여부확인과 팔로잉 하기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok = Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user = User.objects.get(id=tok.user_id)
        request.user = user
     # user authentication process
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        if UserFollowing.objects.filter(following_user=comment.user, user=request.user.pk).exists():
            comment.is_following = "True"
            serializer = isfollowingcommentSerializer(comment)
        else:
            comment.is_following = "False"
            serializer = isfollowingcommentSerializer(comment)
        return Response(serializer.data)

    if request.method == 'POST':
        if UserFollowing.objects.filter(following_user=comment.user, user=request.user.pk).exists():
            # following canceled
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=comment.user_id)
            followee_people.followee_num -= 1
            following_people.follower_num -= 1
            followee_people.save()
            following_people.save()
            UserFollowing.objects.filter(user_id=request.user.pk).delete()
            return Response("following canceled")
        else:
            # following
            serializer = UserFollowingSerializer(data=request.data)
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=comment.user_id)
            user = request.user.pk
            following_user = comment.user_id
            a = {"user": user, "following_user": following_user}
            serializer = UserFollowingSerializer(data=a)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            followee_people.followee_num += 1
            following_people.follower_num += 1
            followee_people.save()
            following_people.save()
            return Response("following ")
