import json
import requests
import urllib.request
from django.http import HttpResponse, FileResponse
from urllib.parse import urlparse

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import QnaListSerializer, QnasmalllistSerializer, AnssmalllistSerializer, ProfileqnaSerializer, \
    QnaListforamtSerializer, QnaSerializer, AnsSerializer, likeSerializer, bookmarkSerializer, solveSerializer, \
    like_ansSerializer, UserinfoSerializer, ProfileListSerializer, ProfileSerializer, QnasmallSerializer, \
    AnssmallSerializer, QnadetailSerializer, AnslistSerializer, AnsdetailSerializer, QnaImageSerializer
    
from .models import Qna, Ans, Qnasmall, Anssmall
from rest_framework import viewsets
from profiles.models import Profile
from accounts.models import User
from image_server.models import QnaValidate
from image_server.serializers import QnaImageValidationSerializer

from mysite.utils import jwt_encode
from rest_auth.models import TokenModel
from rest_framework.authtoken.models import Token
from mysite.app_settings import TokenSerializer
import json
import requests
from urllib.parse import urlparse
from django.core.files.base import ContentFile

from django.http import HttpResponse, JsonResponse

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
        profiles = Profile.objects.all()
        if profiles.filter(user_id=request.user.id).exists():
            pro=profiles.get(user_id=request.user.id)
            request.data['profile'] = pro.id
        serializer = QnaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()    


        qnas = Qna.objects.all()
        image_list = []
        for qna in qnas:
            post_content = QnaImageSerializer(qna).data['content']
            for word in range(1, len(post_content)):
                if post_content[word - 1: word + 1] == '(h':
                    start_idx = word
                if post_content[word] == ')':
                    if start_idx:
                        if post_content[start_idx: word] not in ['http://', 'https://'] and post_content[start_idx: word][-3:] in ['jpg', 'png', 'jpeg', 'gif', 'svg']:
                            image_list.append(post_content[start_idx: word])

        qnavalidate = QnaValidate()
        for url in image_list:
            image_url = url
            name = urlparse(image_url).path.split('/')[-1]
            response = requests.get(image_url) 

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
        qna.bookmarked="False"
       
    if request.method == 'GET':
        serializer = QnadetailSerializer(qna)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QnaSerializer(qna, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
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
    # if request.user.is_authenticated:
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
        

        