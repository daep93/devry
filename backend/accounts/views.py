import json
import requests

from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from allauth.account.forms import ResetPasswordForm

from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView, LogoutView




from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache

from django.contrib.auth import get_user_model, authenticate
from django.template import RequestContext
from django.shortcuts import render                                                            
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.core.mail.message import EmailMessage

from .models import User, Profile
from .serializers import ProfileStatusSerializer, UpdateUserSerializer, UserRegistrationSerializer, UserSerializer, InfoSerializer, deleteSerializer





class UserSignupView(RegisterView):
    """
    유저네임, 이메일, 비밀번호를 입력해 가입할 수 있습니다.
    """
    serializer_class = UserRegistrationSerializer

        
class UserLoginView(LoginView):
    """
    이메일과 비밀번호를 통해 토큰을 발급받을 수 있습니다.
    """

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        self.login()

        return self.get_response()

class UserLogoutView(LogoutView):
    """
    headers에 유저의 토큰을 입력합니다. 
    headers={'Authorization': 'Token your_token'}
    """
    pass


class UserInfoView(APIView):
    """
    이메일과 유저네임을 통해 특정 유저의 정보를 얻을 수 있습니다. 
    {
        "username": "username",
        "email": "email"
    }
    """
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = InfoSerializer(data=request.data)
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
        }
        return Response(response, status=status.HTTP_200_OK)
        

class ProfileList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    # serializer_class = 

# class ProfileList(generics.ListAPIView):
    # User = get_user_model()
    # profile_user = User.objects.get(pk=User.id)
    # serializer_class = ProfileStatusSerializer
    # permission_classes = [IsAuthenticated]
    # queryset = Profile.objects.all()


class UpdateUser(generics.UpdateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = get_user_model().objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj


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
