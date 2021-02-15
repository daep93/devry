import json
import requests
import urllib.request
from django.http import HttpResponse, FileResponse
from urllib.parse import urlparse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import QnaListSerializer, QnasmalllistSerializer, AnssmalllistSerializer, ProfileqnaSerializer, \
    QnaListforamtSerializer, QnaSerializer, AnsSerializer, likeSerializer, bookmarkSerializer, solveSerializer, \
    like_ansSerializer, UserinfoSerializer, ProfileListSerializer, ProfileSerializer, QnasmallSerializer, \
    AnssmallSerializer, QnadetailSerializer, AnslistSerializer, AnsdetailSerializer,AnslistformatSerializer, pinnedSerializer, \
    QnaImageSerializer, AnsImageSerializer, ImagePostSerializer, isfollowingSerializer,isfollowingansSerializer

from accounts.serializers import UserFollowingSerializer
from wsgiref.util import FileWrapper
from image_server.models import QnaValidate, AnsValidate
from image_server.serializers import QnaImageValidationSerializer, AnsImageValidationSerializer
from .models import Qna, Ans, Qnasmall, Anssmall, ImagePost
from rest_framework import viewsets
from profiles.models import Profile
from accounts.models import User, UserFollowing
from mysite.utils import jwt_encode
from rest_auth.models import TokenModel
from rest_framework.authtoken.models import Token
from mysite.app_settings import TokenSerializer
import json
import requests
from urllib.parse import urlparse
from django.core.files.base import ContentFile
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from PIL import Image
from django.http import HttpResponse, JsonResponse
from django.conf import settings


class ImagePostView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ImagePostSerializer
    
    def post(self, request, *args, **kwargs):
        headers = {'Content-Type': 'multipart/form-data; charset=utf-8'}
        user = request.user
        print(user)
        serializer = ImagePostSerializer(data=request.data)
        if serializer.is_valid():
            queryset = ImagePost.objects.all()
            for i in queryset:
                print(ImagePostSerializer(i).data['image'])
                
            print(serializer.validated_data['image'])
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ImagePostViewSet(viewsets.ModelViewSet):
    '''
    사진을 전송받으면 해당 사진을 서버에 저장하고, 해당 이미지의 URL을 돌려줍니다.
    해당 URL을 클릭하면 이미지를 확인할 수 있습니다.
    '''
    queryset = ImagePost.objects.all()
    serializer_class = ImagePostSerializer
    parser_classes = [MultiPartParser, FormParser] 
    

class PostViewSet(viewsets.ModelViewSet):
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Ans.objects.all()
    serializer_class = AnsSerializer


class QnasmallViewSet(viewsets.ModelViewSet):
    queryset = Qnasmall.objects.all()
    serializer_class = QnasmallSerializer


class AnssmallViewSet(viewsets.ModelViewSet):
    queryset = Anssmall.objects.all()
    serializer_class = AnssmallSerializer


@api_view(['GET'])
def qna_list(request):
    """
    Qna(질문 글) 글 목록 보기

    ---
    """
    if request.method == 'GET':
        # 토큰을 이용한 사용자 획인 코드
        if request.META.get('HTTP_AUTHORIZATION'):           
            tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
            user=User.objects.get(id=tok.user_id)
            request.user = user
       
        qnas = Qna.objects.all() 
        for qna in qnas:
            qna.like_num = qna.like_users.count() 
            if qna.like_users.filter(id=request.user.pk).exists():
                qna.liked = "True"      
            else:
                qna.liked = "False"
            qna.ref_tags=list(qna.ref_tags)
            qna.save()
             
        # qna number in user_id -> It will be "True"
        serializer = QnaListforamtSerializer(qnas, many=True)
        return Response(serializer.data) 


@api_view(['GET', 'POST'])
def qna_list_create(request):
    """
    Qna(질문 글) 글 작성

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        qnas = Qna.objects.all()
        for qna in qnas:
            qna.like_num = qna.like_users.count() 
            if qna.like_users.filter(id=request.user.pk).exists():
                qna.liked = "True"      
            else:
                qna.liked = "False"
            qna.save()
            # qna number in user_id -> It will be "True"
        serializer = QnaListSerializer(qnas, many=True)
        return Response(serializer.data) 
    else:
        # print(request.FILES)
        profiles = Profile.objects.all()
        if profiles.filter(user_id=request.user.id).exists():
            pro=profiles.get(user_id=request.user.id)
            request.data['profile'] = pro.id
        serializer = QnaSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()    
            post_qna = Qna.objects.all()
            qna = Qna.objects.get(id=QnaSerializer(post_qna[len(post_qna) - 1]).data['id'])
            image_list = []
            post_content = QnaImageSerializer(qna).data['content']
            for word in range(1, len(post_content)):
                if post_content[word - 1: word + 1] == '(h':
                    start_idx = word
                if post_content[word] == ')':
                    if start_idx:
                        if post_content[start_idx: word][-3:] in ['jpg', 'png', 'jpeg', 'gif', 'svg']:
                            image_list.append(post_content[start_idx: word])
            qnavalidate = QnaValidate()
            print(image_list)
            for url in image_list:
                image_url = url
                name = urlparse(image_url).path.split('/')[-1]
                response = requests.get(image_url) 
                print(name)
                if response.status_code == 200:
                    qnavalidate.qna_image.save(name, ContentFile(response.content), save=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def qna_detail_update_delete(request, qna_pk):
    """
    Qna(post) 상세보기,수정,삭제

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    qna = get_object_or_404(Qna, pk=qna_pk)
    qna.like_num = qna.like_users.count()  # like_num check
    qna.bookmark_num = qna.bookmark_users.count()  # bookmark_num check
    qna.viewed_num = qna.viewed_num + 1 # viewed_num++
    qna.save()

    # url = urlparse('http://localhost:8080/#/qna-detail/'+str(qna_pk))
    # print(url)

    # like_check
    anss = Ans.objects.all()
    for ans in anss:
        ans.like_ans_num = ans.like_ans_users.count()
        if ans.like_ans_users.filter(id=request.user.pk).exists():
            ans.liked_ans = "True"      
        else:
            ans.liked_ans = "False"
        ans.save()
    if qna.like_users.filter(pk=request.user.pk).exists():
        qna.liked="True"
    else:
        qna.liked="False"
    # bookmark_check
    if qna.bookmark_users.filter(pk=request.user.pk).exists():
        qna.bookmarked="True"
    else:
        qna.bookmarked = "False"
        
    if UserFollowing.objects.filter(following_user= qna.user, user=request.user.pk).exists():
        qna.is_following="True"
    else:
        qna.is_following = "False"
        
    if request.method == 'GET':
        serializer = QnadetailSerializer(qna)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QnaSerializer(qna, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        qnavalidate = QnaValidate.objects.get(id=qna_pk)
        qnavalidate.qna_image.delete(save=True)
        qna.delete()
        return Response({ 'id': qna_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def create_ans(request, qna_pk):
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    qna = get_object_or_404(Qna, pk=qna_pk)
    serializer = AnsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(qna=qna)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def ans_list(request):
    """
    큰댓글(답변) 목록 불러오기 및 큰 댓글 작성

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        anss = Ans.objects.all()
        for ans in anss:
            ans.like_ans_num = ans.like_ans_users.count()
            if ans.like_ans_users.filter(id=request.user.pk).exists():
                ans.liked_ans = "True"      
            else:
                ans.liked_ans = "False"
            ans.save()
        anss = Ans.objects.all()
        serializer = AnslistSerializer(anss, many=True)
        return Response(serializer.data)
    else:
        profiles = Profile.objects.all()
        if profiles.filter(user_id=request.user.id).exists():
            pro=profiles.get(user_id=request.user.id)
            request.data['profile'] = pro.id
        serializer = AnsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()     
            post_ans = Ans.objects.all()
            ans = Ans.objects.get(id=AnsSerializer(post_ans[len(post_ans) - 1]).data['id'])
            image_list = []
            post_content = AnsImageSerializer(ans).data['content']
            for word in range(1, len(post_content)):
                if post_content[word - 1: word + 1] == '(h':
                    start_idx = word
                if post_content[word] == ')':
                    if start_idx:
                        if post_content[start_idx: word][-3:] in ['jpg', 'png', 'jpeg', 'gif', 'svg']:
                            image_list.append(post_content[start_idx: word])
            ansvalidate = AnsValidate()
            print(image_list)
            for url in image_list:
                image_url = url
                name = urlparse(image_url).path.split('/')[-1]
                response = requests.get(image_url) 
                print(name)
                if response.status_code == 200:
                    ansvalidate.ans_image.save(name, ContentFile(response.content), save=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def ans_detail_update_delete(request, ans_pk):
    """
    ans 큰댓글(답변) 상세보기,수정,삭제

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    ans = get_object_or_404(Ans, pk=ans_pk)
    if request.method == 'GET':
        serializer = AnsdetailSerializer(ans)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AnsdetailSerializer(ans, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        ansvalidate = AnsValidate.objects.get(id=ans_pk)
        ansvalidate.ans_image.delete(save=True)
        ans.delete()
        return Response({ 'id': ans_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def like(request, qna_pk):
    """
    Qna(질문 글) 좋아요

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    # user authentication process
    qna = get_object_or_404(Qna, pk=qna_pk)
    if request.method == 'GET':
        if qna.like_users.filter(pk=request.user.pk).exists():
            qna.liked="True"
            serializer = likeSerializer(qna)
        else:
            qna.liked="False"
            serializer = likeSerializer(qna)
        return Response(serializer.data)

    # user가 qna을 좋아요 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if qna.like_users.filter(pk=request.user.pk).exists():
            # like canceled
            qna.like_users.remove(request.user)
            return Response("like canceled")
        else:
            # like 
            qna.like_users.add(request.user)
            return Response("like !!!!!!")


@api_view(['GET','POST'])
def pinned(request, qna_pk):
    '''
    Qna(질문 글) pinned
    '''
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    # user authentication process
    qna = get_object_or_404(Qna, pk=qna_pk)
    if request.method == 'GET':
        if qna.pinned_users.filter(pk=request.user.pk).exists():
            qna.pinned="True"
            serializer = pinnedSerializer(qna)
        else:
            qna.pinned="False"
            serializer = pinnedSerializer(qna)
        return Response(serializer.data)

    # user가 qna을 pinned한 전체유저에 존재하는지.
    if request.method == 'POST':
        if qna.pinned_users.filter(pk=request.user.pk).exists():
            # pinned canceled
            qna.pinned_users.remove(request.user)
            return Response("pinned canceled")
        else:
            # pinned 
            qna.pinned_users.add(request.user)
            return Response("pinned !!!!!!")


@api_view(['GET','POST'])
def like_ans(request, ans_pk):
    """
    Ans(큰댓글) 좋아요

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    # user authentication process
    ans = get_object_or_404(Ans, pk=ans_pk)
    if request.method == 'GET':
        if ans.like_ans_users.filter(pk=request.user.pk).exists():
            ans.liked_ans="True"
            serializer = like_ansSerializer(ans)
        else:
            ans.liked_ans="False"
            serializer = like_ansSerializer(ans)
        return Response(serializer.data)

    # user가 ans 좋아요 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if ans.like_ans_users.filter(pk=request.user.pk).exists():
            # like canceled
            ans.like_ans_users.remove(request.user)
            return Response("ans_like canceled")
        else:
            # like 
            ans.like_ans_users.add(request.user)
            return Response("ans_like !!!!!!")


@api_view(['GET','POST'])
def bookmark(request, qna_pk):
    """
    Qna(질문글)) 북마크 기능

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    qna = get_object_or_404(Qna, pk=qna_pk)
    if request.method == 'GET':
        if qna.bookmark_users.filter(pk=request.user.pk).exists():
            qna.bookmarked="True"
            serializer = bookmarkSerializer(qna)
        else:
            qna.bookmarked="False"
            serializer = bookmarkSerializer(qna)
        return Response(serializer.data)

    # user가 qna을 북마크 누른 전체유저에 존재하는지.
    if request.method == 'POST':
        if qna.bookmark_users.filter(pk=request.user.pk).exists():
            # bookmark cancled
            qna.bookmark_users.remove(request.user)
            return Response("bookmark cancled")
        else:
            # bookmark
            qna.bookmark_users.add(request.user)
            return Response("bookmark")


@api_view(['GET','POST'])
def solve(request, ans_pk):
    """
    답변(Ans 큰댓글) 채택

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
 
    ans = get_object_or_404(Ans, pk=ans_pk)
    qna = get_object_or_404(Qna, pk=ans.qna_id)
    if request.method == 'GET':
        serializer = solveSerializer(ans)
        return Response(serializer.data)
    if request.method == 'POST':
        ans = get_object_or_404(Ans, pk=ans_pk)
        qna = get_object_or_404(Qna, pk=ans.qna_id)   
        if ans.assisted == 1:
            ans.assisted = "False"
            qna.solved = "False"
            ans.save()
            qna.save()
            return Response("sovled canceled")

        elif ans.assisted == 0:
            ans.assisted = "True"
            qna.solved = "True"
            ans.save()
            qna.save()
            return Response("sovled!!!!!!!!")
        return Response("오류!!!!!!!!")


@api_view(['GET'])
def qna_list_small(request):
    """
    Qna(질문글)에 달리는 작은 댓글 모두보기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        anss = Qnasmall.objects.all()
        serializer = QnasmalllistSerializer(anss, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def qna_list_small_q(request, qna_pk):
    """
    Qna(질문글 큰댓글)) **특정 질문 글에 달린 작은댓글 모두 보기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        anss = Qnasmall.objects.all()
        an=anss.filter(qna_id=qna_pk)
        serializer = QnasmalllistSerializer(an, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def qna_list_create_small(request):
    """
    Qna(질문글))에 달리는 작은 댓글 작성

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        anss = Qnasmall.objects.all()
        serializer = QnasmallSerializer(anss, many=True)
        return Response(serializer.data)
    else:
        serializer = QnasmallSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()     
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def qna_detail_update_delete_small(request, qnasmall_pk):
    """
    Qna(질문글))에 달리는 작은 댓글 상세보기,수정,삭제

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    qnasmall = get_object_or_404(Qnasmall, pk=qnasmall_pk)
    if request.method == 'GET':
        serializer = QnasmalllistSerializer(qnasmall)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QnasmallSerializer(qnasmall, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        qnasmall.delete()
        return Response({'id': qnasmall_pk}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def ans_list_small(request):
    """
    Ans(큰댓글))에 달리는 작은 댓글 모두보기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        anss = Anssmall.objects.all()
        serializer = AnssmalllistSerializer(anss, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def ans_list_create_small(request):
    """
    Ans(큰댓글))에 달리는 작은 댓글 작성

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        anss = Anssmall.objects.all()
        serializer = AnssmallSerializer(anss, many=True)
        return Response(serializer.data)
    else:
        serializer = AnssmallSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()     
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def ans_list_small_q(request, ans_pk):
    """
    Ans(큰댓글)) **특정 큰댓글에 달린 작은댓글 모두 보기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    if request.method == 'GET':
        anss = Anssmall.objects.all()
        an=anss.filter(ans_id=ans_pk)
        serializer = AnssmalllistSerializer(an, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def ans_detail_update_delete_small(request, anssmall_pk):
    """
    Ans(큰댓글))에 달리는 작은 댓글 상세보기,수정,삭제

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    anssmall = get_object_or_404(Anssmall, pk=anssmall_pk)
    if request.method == 'GET':
        serializer = AnssmalllistSerializer(anssmall)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AnssmallSerializer(anssmall, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        anssmall.delete()
        return Response({'id': anssmall_pk}, status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET'])
def qna_mybookmark(request):
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
        qnas = Qna.objects.all()
        for qna in qnas:
            if qna.bookmark_users.filter(id=request.user.pk).exists():
                mark.append(qna)
        serializer = QnaListforamtSerializer(mark, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def qna_myqna(request):
    """
    내가 작성한 qna 작성 글 목록 불러오기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user

    if request.method == 'GET':
        qna = Qna.objects.filter(user_id=request.user.pk)
        serializer = QnaListforamtSerializer(qna, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def qna_myans(request):
    """
    내가 작성한 ans 작성 큰댓글 목록 불러오기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user = user

    if request.method == 'GET':
        ans = Ans.objects.filter(user_id=request.user.pk)
        serializer = AnslistformatSerializer(ans, many=True)
        return Response(serializer.data)
        

@api_view(['GET','POST'])
def is_following(request, qna_pk):
    """
    Qna(질문 글) 작성자 팔로잉 여부확인과 팔로잉 하기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
    # user authentication process
    qna = get_object_or_404(Qna, pk=qna_pk)
    if request.method == 'GET':
        if UserFollowing.objects.filter(following_user= qna.user, user=request.user.pk).exists():
            qna.is_following="True"
            serializer = isfollowingSerializer(qna)
        else:
            qna.is_following="False"
            serializer = isfollowingSerializer(qna)
        return Response(serializer.data)
        
    if request.method == 'POST':
        if UserFollowing.objects.filter(following_user= qna.user, user=request.user.pk).exists():
            # following canceled
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=qna.user_id)
            followee_people.follower_num -= 1
            following_people.followee_num -= 1
            followee_people.save()
            following_people.save()
            UserFollowing.objects.filter(user_id=request.user.pk).delete()     
            return Response("following canceled")
        else:
            # following 
            serializer = UserFollowingSerializer(data=request.data)
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=qna.user_id)
            user =request.user.pk
            following_user = qna.user_id
            a={"user":user,"following_user":following_user}
            serializer = UserFollowingSerializer(data=a)  
            if serializer.is_valid(raise_exception=True):
                serializer.save()     
            followee_people.follower_num += 1
            following_people.followee_num += 1
            followee_people.save()
            following_people.save()
            return Response("following ")


@api_view(['GET','POST'])
def is_following_ans(request, ans_pk):
    """
    Ans(큰 댓글) 작성자 팔로잉 여부확인과 팔로잉 하기

    ---
    """
    if request.META.get('HTTP_AUTHORIZATION'):
        tok=Token.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        user=User.objects.get(id=tok.user_id)
        request.user=user
     # user authentication process
    ans = get_object_or_404(Ans, pk=ans_pk)
    if request.method == 'GET':
        if UserFollowing.objects.filter(following_user= ans.user, user=request.user.pk).exists():
            ans.is_following="True"
            serializer = isfollowingansSerializer(ans)
        else:
            ans.is_following="False"
            serializer = isfollowingansSerializer(ans)
        return Response(serializer.data)
        
    if request.method == 'POST':
        if UserFollowing.objects.filter(following_user= ans.user, user=request.user.pk).exists():
            # following canceled
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=ans.user_id)
            followee_people.follower_num -= 1
            following_people.followee_num -= 1
            followee_people.save()
            following_people.save()
            UserFollowing.objects.filter(user_id=request.user.pk).delete()
            return Response("following canceled")
        else:
            # following 
            serializer = UserFollowingSerializer(data=request.data)
            followee_people = User.objects.get(pk=request.user.pk)
            following_people = User.objects.get(pk=ans.user_id)
            user =request.user.pk
            following_user = ans.user_id
            a={"user":user,"following_user":following_user}
            serializer = UserFollowingSerializer(data=a)  
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            followee_people.follower_num += 1
            following_people.followee_num += 1
            followee_people.save()
            following_people.save()
            return Response("following ")