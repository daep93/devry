from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.serializers import UserSerializer, UserProfileUpdateSerializer
from accounts.models import User
from .serializers import ProfileSerializer, ProfileListSerializer
from .models import Profile
from rest_framework import viewsets

from articles.models import Article, Comment
from articles.serializers import ArticleProfileSerializer, CommentProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        print(request.data)
        profile_user = User.objects.get(pk=request.data['user'])
        profile_user_data = {
            'username': request.data['username'],
            'email': UserProfileUpdateSerializer(profile_user).data['email'],
        }
        profile_user_serailzer = UserProfileUpdateSerializer(profile_user, data=profile_user_data)
        print(profile_user_data['username'])
        if profile_user_serailzer.is_valid(raise_exception=True):
            profile_user_serailzer.save()
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def profile_list_create(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileListSerializer(profiles, many=True)
        return Response(serializer.data)
        
    else:
        serializer = ProfileSerializer(data=request.data)
        print(request.data)
        profile_user = User.objects.get(pk=request.data['user'])
        profile_user_data = {
            'username': request.data['username'],
            'email': UserProfileUpdateSerializer(profile_user).data['email'],
        }
        profile_user_serailzer = UserProfileUpdateSerializer(profile_user, data=profile_user_data)
        print(profile_user_data['username'])
        if profile_user_serailzer.is_valid(raise_exception=True):
            profile_user_serailzer.save()
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def profile_detail_update_delete(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk) 
    comments = Comment.objects.all()

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        articles = Article.objects.filter(author=ProfileSerializer(profile).data['user'])
        comments = Comment.objects.filter(user=ProfileSerializer(profile).data['user'])

        for article in articles:
            serializer.data['posts'].append(ArticleProfileSerializer(article).data)

        for comment in comments:
            serializer.data['comments'].append(CommentProfileSerializer(comment).data)

        return Response(serializer.data)

    if request.method == 'PUT':
        profile_user = User.objects.get(pk=request.data['user'])
        serializer = ProfileSerializer(profile, data=request.data)

        profile_user_data = {
            'username': request.data['username'],
            'email': UserProfileUpdateSerializer(profile_user).data['email'],
        }
        profile_user_serailzer = UserProfileUpdateSerializer(profile_user, data=profile_user_data)

        if profile_user_serailzer.is_valid(raise_exception=True):
            profile_user_serailzer.save()

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 

