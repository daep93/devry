from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.serializers import UserSerializer, UserProfileUpdateSerializer, TokenSerializer, UserJoinedSerializer
from accounts.models import User
from .serializers import ProfileSerializer, ProfileListSerializer, ProfileLinkSerializer, ProfileProjectSerializer, ProfileUpdateSerializer, ProfileShowSerializer
from .models import Profile
# from .models import Profile, Link, Project
from rest_framework import viewsets

from accounts.models import UserFollowing
from accounts.serializers import UserFollowingSerializer
from articles.models import Article, Comment
from articles.serializers import ArticleProfileSerializer, CommentProfileSerializer, PinnedPostsProfileSerializer, ArticleSerializer, PinnedUsersProfileSerializer
from qnas.serializers import QnaSerializer, ProfileQnaSerializer
from qnas.models import Qna
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
        target_user = User.objects.get(pk=request.data['user'])
        target_user_joined = UserSerializer(target_user).data['date_joined']

        follows = UserFollowing.objects.all()
        print(follows)

        for follow in follows:

            if UserFollowingSerializer(follow).data['user'] == UserSerializer(target_user).data['id']:
                target_user.follower_num += 1
            if UserFollowingSerializer(follow).data['following_user'] == UserSerializer(target_user).data['id']:
                target_user.followee_num += 1
        print(target_user.follower_num)
        print(target_user.followee_num)

        if serializer.is_valid(raise_exception=True):

            serializer.validated_data['follower_num'] = target_user.follower_num
            serializer.validated_data['followee_num'] = target_user.followee_num 
            serializer.validated_data['joined'] = target_user_joined
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile_show(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk) 
    comments = Comment.objects.all()

    real_tags = []
    tags_list = {
        'Python3': 0,
        'Django': 0,
        'Java': 0,
        'Spring': 0,
        'HTML5': 0,
        'CSS3': 0,
        'JavaScript': 0,
        'TypeScript': 0,
        'Vue.js': 0,
        'React': 0,
        'Angular': 0,
        'Node.js': 0,
        'Swift': 0,
        'Ruby': 0,
        'Ruby on Rails': 0,
        'MySQL': 0,
        'MariaDB': 0,
        'MongoDB': 0,
        'Docker': 0,
        'Kubernetes': 0,
        'FrontEnd': 0,
        'BackEnd': 0,
        'DevOps': 0,
        'Artificial Intelligence': 0,
        'BigData': 0,
        'Blockchain': 0,
        'Internet of Things': 0,
        'Augmented Reality': 0,
        'Virtual Reality': 0
    }

    if request.method == 'GET':
        serializer = ProfileShowSerializer(profile)
        email = User.objects.filter(pk=ProfileSerializer(profile).data['user']).first()
        profile_user = User.objects.get(pk=ProfileSerializer(profile).data['user'])
        serializer.data['joined'] = UserSerializer(email).data['date_joined']
        target_user = User.objects.get(username=email)

        follows = UserFollowing.objects.all()

        for follow in follows:

            if UserFollowingSerializer(follow).data['user'] == UserSerializer(target_user).data['id']:
                target_user.follower_num += 1
                serializer.data['follower_num'] += 1
            if UserFollowingSerializer(follow).data['following_user'] == UserSerializer(target_user).data['id']:
                target_user.followee_num += 1
                serializer.data['followee_num'] += 1

        serializer.data['follower_num'] = (target_user.follower_num)
        serializer.data['followee_num'] = target_user.followee_num 

        all_qnas = Qna.objects.filter(author=ProfileSerializer(profile).data['user'])
        for some_qna in all_qnas:
            if ProfileSerializer(profile).data['user'] == QnaSerializer(some_qna).data['author']:
                for ref in QnaSerializer(some_qna).data['ref_tags']:
                    tags_list[ref] += 1

        # all_articles = Article.objects.filter(author=ProfileSerializer(profile).data['user'])
        # for some_article in all_articles:
        #     if ProfileSerializer(profile).data['user'] == ArticleSerializer(some_article).data['author']:
        #         for ref in ArticleSerializer(some_article).data['tags']:
        #             tags_list[ref] += 1

        for single_tag in tags_list:
            if tags_list[single_tag] > 0:
                real_tags.append({single_tag: tags_list[single_tag]})

        print(tags_list)
        print(real_tags)
        print(ProfileShowSerializer(profile).data)




        # articles = Article.objects.filter(author=ProfileSerializer(profile).data['user'])
        qnas = Qna.objects.filter(author=ProfileSerializer(profile).data['user'])
        comments = Comment.objects.filter(user=ProfileSerializer(profile).data['user'])
        pinned_posts = Article.objects.filter(author=ProfileSerializer(profile).data['user'])
        links = {
                'sns_name1': ProfileSerializer(profile).data['sns_name1'], 
                'sns_url1': ProfileSerializer(profile).data['sns_url1'],
                'sns_name2': ProfileSerializer(profile).data['sns_name2'], 
                'sns_url2': ProfileSerializer(profile).data['sns_url2'],
                'sns_name3': ProfileSerializer(profile).data['sns_name3'], 
                'sns_url3': ProfileSerializer(profile).data['sns_url3']
        }
        projects = {
                'project_name1': ProfileSerializer(profile).data['project_name1'], 
                'project_url1': ProfileSerializer(profile).data['project_url1'],
                'project_name2': ProfileSerializer(profile).data['project_name2'], 
                'project_url2': ProfileSerializer(profile).data['project_url2'],
                'project_name3': ProfileSerializer(profile).data['project_name3'], 
                'project_url3': ProfileSerializer(profile).data['project_url3']
        }

        for qna in qnas:
            serializer.data['posts'].append(ProfileQnaSerializer(qna).data)

        for comment in comments:
            serializer.data['comments'].append(CommentProfileSerializer(comment).data)

        for pinned_post in pinned_posts:
            if ProfileSerializer(profile).data['user'] in PinnedUsersProfileSerializer(pinned_post).data['pinned_users']:
                serializer.data['pinned_posts'].append(PinnedPostsProfileSerializer(pinned_post).data)

        for real in real_tags:
            serializer.data['tags'].update(real)

        serializer.data['links'].append(links)
        serializer.data['projects'].append(projects)
        return Response(serializer.data)

 

@api_view(['GET', 'PUT'])
def profile_setting(request, profile_pk):  
    '''
    사용자로부터 넘어오는 토큰 값(request.META['HTTP_AUTHORIZATION'])이 서버에 저장된 사용자의 토큰(TokenSerializer(user.auth_token).data['key'])과 일치하면
    프로필 정보를 보여주거나, 수정할 수 있습니다.
    '''

    profile = get_object_or_404(Profile, pk=profile_pk)

    user = User.objects.filter(pk=ProfileSerializer(profile).data['user']).first()
    links = {
            'sns_name1': ProfileSerializer(profile).data['sns_name1'], 
            'sns_url1': ProfileSerializer(profile).data['sns_url1'],
            'sns_name2': ProfileSerializer(profile).data['sns_name2'], 
            'sns_url2': ProfileSerializer(profile).data['sns_url2'],
            'sns_name3': ProfileSerializer(profile).data['sns_name3'], 
            'sns_url3': ProfileSerializer(profile).data['sns_url3']
    }
    projects = {
            'project_name1': ProfileSerializer(profile).data['project_name1'], 
            'project_url1': ProfileSerializer(profile).data['project_url1'],
            'project_name2': ProfileSerializer(profile).data['project_name2'], 
            'project_url2': ProfileSerializer(profile).data['project_url2'],
            'project_name3': ProfileSerializer(profile).data['project_name3'], 
            'project_url3': ProfileSerializer(profile).data['project_url3']
    }
    # request.META['HTTP_AUTHORIZATION'] = '17d6c8c6e992e129009f608936f0a98c7312dcee'
    if request.META['HTTP_AUTHORIZATION'] == TokenSerializer(user.auth_token).data['key']:
        if request.method == 'GET':
            serializer = ProfileListSerializer(profile)

            # email_user = User.objects.get(pk=ProfileListSerializer(profile).data['user'])

            serializer.data['links'].append(links)
            serializer.data['projects'].append(projects)

            return Response(serializer.data)

        if request.method == 'PUT':

            links = {
                    'sns_name1': request.data['sns_name1'], 
                    'sns_url1': request.data['sns_url1'],
                    'sns_name2': request.data['sns_name2'], 
                    'sns_url2': request.data['sns_url2'],
                    'sns_name3': request.data['sns_name3'], 
                    'sns_url3': request.data['sns_url3']
            }
            projects = {
                    'project_name1': request.data['project_name1'], 
                    'project_url1': request.data['project_url1'],
                    'project_name2': request.data['project_name2'], 
                    'project_url2': request.data['project_url2'],
                    'project_name3': request.data['project_name3'], 
                    'project_url3': request.data['project_url3']
            }

            serializer = ProfileUpdateSerializer(profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # serializer.data['links'].append(links)
                # serializer.data['projects'].append(projects)    
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response('잘못된 요청입니다.', status=status.HTTP_400_BAD_REQUEST)
    