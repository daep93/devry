from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import QnaListSerializer, QnaSerializer, AnsSerializer
from .models import Qna, Ans
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Ans.objects.all()
    serializer_class = AnsSerializer


@api_view(['GET', 'POST'])
def qna_list_create(request):
    if request.method == 'GET':
        qnas = Qna.objects.all()
        serializer = QnaListSerializer(qnas, many=True)
        return Response(serializer.data)
        
    else:
        serializer = QnaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def qna_detail_update_delete(request, qna_pk):
    qna = get_object_or_404(Qna, pk=qna_pk)
    if request.method == 'GET':
        serializer = QnaSerializer(qna)
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
def create_comment(request, qna_pk):
    qna = get_object_or_404(Qna, pk=qna_pk)
    serializer = AnsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(qna=qna)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_list(request):
    anss = Ans.objects.all()
    serializer = AnsSerializer(anss, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, ans_pk):
    ans = get_object_or_404(Ans, pk=ans_pk)
    if request.method == 'GET':
        serializer = AnsSerializer(ans)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AnsSerializer(ans, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    else:
        ans.delete()
        return Response({ 'id': ans_pk }, status=status.HTTP_204_NO_CONTENT)