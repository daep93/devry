from django.shortcuts import get_object_or_404
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import User

# Create your views here.

# 계정 생성 API
class UserCreateAPI(generics.CreateAPIView):
    serializer_class=UserRegisterSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# 계정 로그인 API
class UserLoginAPI(generics.CreateAPIView):
    serializer_class=UserLoginSerializer
    def post(self, request):
        context={}
        email=request.POST.get('username')
        password=request.POST.get('password')
        # 사용자의 정보를 맞추어보고 해당 user가 있으면 반환한다.
        user=authenticate(email=email, password=password)
        
        if user:
            try:
                token=Token.objects.get(user=user)
            except Token.DoesNotExist:
                toekn=Token.objects.create(user=user)
            context['response']="성공적으로 인증되었습니다"
            context['id']=user.id
            context['email']=email
            context['token']=token.key
        else:
            context['response']="에러가 발생했습니다"
            context['error_message']="인증에 실패했습니다"
        return Response(context, status=status.HTTP_404_NOT_FOUND)

        
