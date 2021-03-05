from django.shortcuts import get_object_or_404
from rest_framework import generics,status
from .models import Qna
from accounts.models import Profile
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import (
    QnaListSerializer,
    QnaRegisterSerializer
)
# Create your views here.
class QnaListAPI(generics.ListAPIView):
    serializer_class=QnaListSerializer

    def get_queryset(self):
        return Qna.objects.all()

class QnaCreateAPI(generics.CreateAPIView):
    serializer_class=QnaRegisterSerializer
    authentication_classes=[TokenAuthentication]
    def post(self, request):
        
        profile=get_object_or_404(Profile, user=request.user)
        data=request.data.copy()
        data["writer"] = profile.id
        #TODO: vue.js를 통해서 실제로 데이터가 문자열이 아닌 배열로 들어온다면 해당 로직을 바꿔야한다.
        data['ref_tags']='|'.join(data['ref_tags'].split(','))
        serializer = QnaRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

