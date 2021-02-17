import requests
import json

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostListSerializer, ProfilepostSerializer, PostListforamtSerializer, PostSerializer,CommentSerializer, likeSerializer, bookmarkSerializer, like_commentSerializer, \
    UserinfoSerializer,ProfileListSerializer ,PostdetailSerializer,CommentlistSerializer,CommentdetailSerializer, PostDetailCommentSerializer, DetailCommentSerializer, pinnedSerializer,  \
        ProfilepostSerializer, ForumPostSerializer, pinnedDetailSerializer, PostMentionedCommentSerializer, DetailCommentMentionedSerializer, MentionedCommentSerializer, MentionedUserInfoSerializer
from .models import Post, Comment
from rest_framework import viewsets
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from accounts.models import User, Mentioned
from accounts.serializers import UserSerializer
from qnas.models import Qna
from qnas.serializers import QnapinnedSerializer, QnaDetailPinnedSerializer

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
        comment_for_post = Comment.objects.filter(post=PostSerializer(post).data['forum_id'])
        post.comment_num = len(comment_for_post)
        post.save()

        post_user = PostSerializer(post).data['user']
        post_username = User.objects.get(id=post_user)
        post_user_profile = Profile.objects.get(username=post_username)

        serializer.data['writer_info'].append(ProfilepostSerializer(post_user_profile).data)

        print(request.FILES)
        if 'thumbnail' in request.FILES:
            image_url = "http://127.0.0.1:8000/qnatest/image/"
            response = requests.post(url=image_url)
            print(response)
            print(response.json())

        user_pinned_posts = []
        forum_for_pinned = Post.objects.all()
        for single_pinned_post in forum_for_pinned:
            if post_user in pinnedSerializer(single_pinned_post).data['pinned_users']:
                user_pinned_posts.append(pinnedDetailSerializer(single_pinned_post).data)
        
        qna_for_pinned = Qna.objects.all()
        for single_pinned_post in qna_for_pinned:
            if post_user in QnapinnedSerializer(single_pinned_post).data['pinned_users']:
                user_pinned_posts.append(QnaDetailPinnedSerializer(single_pinned_post).data)

        for user_pinned_post in range(len(user_pinned_posts)):
            serializer.data['writer_info'][0]['pinned_posts'].append(user_pinned_posts[user_pinned_post])

        serializer.data['forum_post'].append(ForumPostSerializer(post).data)


        
        for single_comment in range(len(comment_for_post)):
            comment_username = User.objects.get(id=DetailCommentSerializer(comment_for_post[single_comment]).data['user'])

            serializer.data['comments'].append(DetailCommentSerializer(comment_for_post[single_comment]).data)

            comment_user_profile = Profile.objects.get(user=DetailCommentSerializer(comment_for_post[single_comment]).data['user'])
            comment_user_img = ProfileSerializer(comment_user_profile).data['profile_img']

            serializer.data['comments'][single_comment]['username'] = str(comment_username)
            serializer.data['comments'][single_comment]['profile_img'] = comment_user_img

            mentioned_comments = Mentioned.objects.filter(comment= serializer.data['comments'][single_comment]['comment_id'])

        for single_mention in range(len(mentioned_comments)):
            mentioned_user = Profile.objects.get(user=MentionedCommentSerializer(mentioned_comments[single_mention]).data['mentioned_user'])
            serializer.data['comments'][0]['mentioned'].append(MentionedUserInfoSerializer(mentioned_user).data)

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
def comment_mentioned(request, comment_pk):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        mentions = Mentioned.objects.all()
        serializer = MentionedCommentSerializer(mentions, many=True)
        return Response(serializer.data)

    else:
        serializer = MentionedCommentSerializer(data=request.data)
        mention_people = User.objects.get(pk=request.data['user'])
        mentioned_people = User.objects.get(pk=request.data['mentioned_user'])

        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            serializer.save()
        

        return Response(serializer.data, status=status.HTTP_200_OK)



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
        serializer = likeSerializer(post)
        if post.like_users.filter(pk=request.user.pk).exists():
            post.liked="True"
            post.save()
        else:
            post.liked="False"
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
        serializer = like_commentSerializer(comment)
        if comment.like_comment_users.filter(pk=request.user.pk).exists():
            comment.liked_comment="True"
            comment.save()
        else:
            comment.liked_comment="False"
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
        serializer = bookmarkSerializer(post)
        if post.bookmark_users.filter(pk=request.user.pk).exists():
            post.bookmarked="True"
            post.save()
        else:
            post.bookmarked="False"
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

@api_view(['GET','POST'])
def pinned(request, post_pk):
    """
    post pinned 기능

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        serializer = pinnedSerializer(post)
        if post.pinned_users.filter(pk=request.user.pk).exists():
            post.pinneded="True"
            post.save()
        else:
            post.pinneded="False"
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
