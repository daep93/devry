from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.serializers import UserSerializer, UserProfileUpdateSerializer, TokenSerializer, UserJoinedSerializer, UserFollowerNumberSerializer
from accounts.models import User
from .serializers import ProfileSerializer, ProfileListSerializer, ProfileLinkSerializer, ProfileProjectSerializer, ProfileUpdateSerializer, ProfileShowSerializer
from .models import Profile
from rest_framework import viewsets

from qnas.serializers import QnaSerializer, AnsSerializer
from qnas.models import Qna, Ans
class PostViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        profile_user = User.objects.get(pk=request.data['user'])
        profile_user_data = {
            # 'username': request.data['username'],
            'email': UserProfileUpdateSerializer(profile_user).data['email'],
        }
        profile_user_serailzer = UserProfileUpdateSerializer(profile_user, data=profile_user_data)

        # print(profile_user_data['username'])
        if profile_user_serailzer.is_valid(raise_exception=True):
            profile_user_serailzer.save()
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def profile_list_create(request):
    '''
    사용자의 profile을 생성할 수 있습니다.
    GET Method의 경우 프로필 정보들을 조회하고, 
    POST Method의 경우 프로필을 생성합니다.
    필수 값은 다음과 같습니다.
    {
        "user": user_pk,
        "teck_stack": ["stack"],
        "tag": ["tag"]
    }
    
    '''
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileListSerializer(profiles, many=True)

        # 프로필에서 저장한 sns_name, sns_url, project_name, project_url들을 각각 links, projects에 담아주는 과정입니다.
        profile_number = 0
        for profile in profiles:
            for number in range(1, 4):
                sns_name = 'sns_name' + str(number)
                sns_url = 'sns_url' + str(number)

                project_name = 'project_name' + str(number)
                project_url = 'project_url' + str(number)

                # sns_name(1 ~ 3), sns_url(1 ~ 3)이 존재하는 경우 -- 하나만 존재하는 경우 추가하지 않음
                if ProfileSerializer(profile).data[sns_name] and ProfileSerializer(profile).data[sns_url]:
                    serializer.data[profile_number]['links'].append({ProfileSerializer(profile).data[sns_name]: ProfileSerializer(profile).data[sns_url]})

                # project_name(1 ~ 3), project_url(1 ~ 3)이 존재하는 경우 -- 하나만 존재하는 경우 추가하지 않음
                if ProfileSerializer(profile).data[project_name] and ProfileSerializer(profile).data[project_url]:
                    serializer.data[profile_number]['projects'].append({ProfileSerializer(profile).data[project_name]: ProfileSerializer(profile).data[project_url]})
            # 1, 2, 3처럼 순서대로 가는 것이 아니라 1, 2, 4번 유저의 프로필이 있고 3번 유저의 프로필이 없는 경우 serializer.data의 인덱스에 연속적인 숫자를 사용하면 인덱스 에러 발생
            profile_number += 1  

        return Response(serializer.data)
        
    else:
        serializer = ProfileSerializer(data=request.data)
        target_user = User.objects.get(pk=request.data['user'])
        target_user_joined = UserJoinedSerializer(target_user).data['date_joined']        # 프로필을 만드려는 사용자가 회원가입한 시점

        if serializer.is_valid(raise_exception=True):

            serializer.validated_data['email'] = UserSerializer(target_user).data['email']
            serializer.validated_data['username'] = UserSerializer(target_user).data['username']
            serializer.validated_data['joined'] = target_user_joined
            # followers, following은 UserSerializer 내부에서 OrderedDict 형태로 확인이 가능합니다. 각각 id, user, following_user, created(팔로잉한 시간)으로 구성되어 있습니다.(accounts.models.py 참고)
            serializer.validated_data['followee_num'] = len(UserSerializer(target_user).data['followers'])   # 사용자를 팔로우하고 있는 사용자들의 수
            serializer.validated_data['follower_num'] = len(UserSerializer(target_user).data['following'])   # 사용자가 팔로우하고 있는 사용자들의 수
        
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile_show(request, profile_pk):
    '''
    GET Method를 통해 사용자의 상세 프로필을 조회합니다. 
    '''
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
        'Frontend': 0,
        'Backend': 0,
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

        
        if len(UserSerializer(profile_user).data['following']):
            # print(len(UserSerializer(profile_user).data['following']))   # 사용자가 팔로잉하는 사용자들
            # print(len(UserSerializer(profile_user).data['followers']))   # 사용자를 팔로우하는 사용자들
            serializer.data['follower_num'] += len(UserSerializer(profile_user).data['following'])
            serializer.data['followee_num'] = len(UserSerializer(profile_user).data['followers'])

        # 모든 qna에서의 글 중 사용자가 쓴 글만 불러오고, 해당 글에서 참조된 태그들을 추가하는 과정
        all_qnas = Qna.objects.filter(user=UserJoinedSerializer(profile).data['id'])
        for some_qna in all_qnas:
            for ref in QnaSerializer(some_qna).data['ref_tags']:
                tags_list[ref] += 1

        # 한 번 이상 추가된 태그들만 남겨놓는 작업
        for single_tag in tags_list:
            if tags_list[single_tag] > 0:
                real_tags.append({single_tag: tags_list[single_tag]})


        qna_data = []

        qnas = Qna.objects.filter(user=ProfileSerializer(profile).data['user'])
        comments = Ans.objects.filter(user=ProfileSerializer(profile).data['user'])

        # pinned_post 부분은 잠시 비워두었습니다. bookmark와 pinned_post가 서로 다른 로직이라면, pinned하는 함수를 하나 더 추가해 적용해야 합니다. 
        # pinned_posts = Article.objects.filter(user=ProfileSerializer(profile).data['user'])    

        for qna in qnas:
            serializer.data['posts'].append(QnaSerializer(qna).data)
        for comment in comments:
            serializer.data['comments'].append(AnsSerializer(comment).data)

        # for pinned_post in pinned_posts:
        #     if ProfileSerializer(profile).data['user'] in PinnedUsersProfileSerializer(pinned_post).data['pinned_users']:
        #         serializer.data['pinned_posts'].append(PinnedPostsProfileSerializer(pinned_post).data)

        print(real_tags)
        for real in real_tags:
            serializer.data['tags'].append(real)

        for number in range(1, 4):
            sns_name = 'sns_name' + str(number)
            sns_url = 'sns_url' + str(number)

            project_name = 'project_name' + str(number)
            project_url = 'project_url' + str(number)

            if ProfileSerializer(profile).data[sns_name] and ProfileSerializer(profile).data[sns_url]:
                serializer.data['links'].append({ProfileSerializer(profile).data[sns_name]: ProfileSerializer(profile).data[sns_url]})

            if ProfileSerializer(profile).data[project_name] and ProfileSerializer(profile).data[project_url]:
                serializer.data['projects'].append({ProfileSerializer(profile).data[project_name]: ProfileSerializer(profile).data[project_url]})

        return Response(serializer.data)

 

@api_view(['GET', 'PUT'])
def profile_setting(request, profile_pk):  
    '''
    사용자로부터 넘어오는 토큰 값(request.META['HTTP_AUTHORIZATION'])이 서버에 저장된 사용자의 토큰(TokenSerializer(user.auth_token).data['key'])과 일치하면
    프로필 정보를 보여주거나, 수정할 수 있습니다.
    '''

    # 현재 PUT 메서드에서 CSRF 관련 오류가 발생하고 있습니다. 빠른 시일 내로 수정하겠습니다. 
    # GET 메서드로 보여주는 기능은 정상적으로 동작합니다. 

    profile = get_object_or_404(Profile, pk=profile_pk)

    user = User.objects.filter(pk=ProfileSerializer(profile).data['user']).first()

    if request.META['HTTP_AUTHORIZATION'] == TokenSerializer(user.auth_token).data['key']:
        if request.method == 'GET':
            serializer = ProfileListSerializer(profile)

            # email_user = User.objects.get(pk=ProfileListSerializer(profile).data['user'])

            for number in range(1, 4):
                sns_name = 'sns_name' + str(number)
                sns_url = 'sns_url' + str(number)

                project_name = 'project_name' + str(number)
                project_url = 'project_url' + str(number)

                if ProfileSerializer(profile).data[sns_name] and ProfileSerializer(profile).data[sns_url]:
                    serializer.data['links'].append({ProfileSerializer(profile).data[sns_name]: ProfileSerializer(profile).data[sns_url]})

                if ProfileSerializer(profile).data[project_name] and ProfileSerializer(profile).data[project_url]:
                    serializer.data['projects'].append({ProfileSerializer(profile).data[project_name]: ProfileSerializer(profile).data[project_url]})


            return Response(serializer.data)

        if request.method == 'PUT':
            serializer = ProfileUpdateSerializer(profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response('잘못된 요청입니다.', status=status.HTTP_400_BAD_REQUEST)
    