from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from allauth.account.forms import ResetPasswordForm




from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache

from django.template import RequestContext
from django.shortcuts import render                                                            
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.core.mail.message import EmailMessage

from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, AuthSerializer, deleteSerializer

INTERNAL_RESET_URL_TOKEN = 'set-password'
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'

import json
import requests

@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(email=serializer.validated_data['email']).first() is None:
            serializer.save()
            return Response({
                'username': serializer.data['username'],
                'email': serializer.data['email'],
            }, status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        email = request.data.get('email')

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        user = User.objects.get(email=email)

        response = {
            'user': {
                'username': UserSerializer(user).data['username'],
                'email': serializer.data['email']
            },
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def auth(request):
    if request.method == 'POST':
        serializer = AuthSerializer(data=request.data)
        email = request.data.get('email')
        username = request.data.get('username')

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'user': {
                'username': serializer.data['username'],
                'email': serializer.data['email'],   
                
            },
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)
        

@api_view(['GET'])
@permission_classes([AllowAny])
def profile(request):
    if request.method == 'GET':
        serializer = UserSerializer
        user = User.objects.get(pk=1)
        print(user)
        print(UserSerializer(user).data['email'])
        response = {
            'username': serializer(user).data['username'],
            'email': serializer(user).data['email'],
            # 'date_joined': serializer(user).data['date_joined'],
        }
        return HttpResponse(response)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete(request):
    if request.method == 'DELETE':
        serializer = deleteSerializer(data=request.data)
        email = request.data.get('email')
        user = User.objects.get(email=email)
        user.delete()
        return Response({'email': email}, status=status.HTTP_204_NO_CONTENT)

# def req(request):
#     credentials = {'username': 'pie3', 'email': 'apple@apple.com3'}
#     response = requests.post("http://127.0.0.1:8000/auth/", data=credentials)
#     return HttpResponse(response)


# class ChangePasswordView(generics.UpdateAPIView):
#     """
#     An endpoint for changing password.
#     """
        
#     serializer_class = ChangePasswordSerializer
#     model = User
#     permission_classes = (permissions.IsAuthenticated,)
#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')

#         if old_password == new_password:
#             return Response('비밀번호 동일', status=status.HTTP_400_BAD_REQUEST)
            
#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }

#             return Response(response)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def send_email(request):
#     subject = "message"
#     to = ["rossro464@gmail.com"]
#     from_email = "rossro464@gmail.com"
#     message = "테스트0"
#     EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html' #템플릿을 변경하려면 이와같은 형식으로 입력
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'accounts/password_reset_done_fail.html')
            
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html' #템플릿을 변경하려면 이와같은 형식으로 입력



class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url=reverse_lazy('password_reset_complete')
    template_name = 'accounts/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = resolve_url(settings.LOGIN_URL)
        return context
