from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import (email_address_exists,
                            get_username_max_length)

from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import update_last_login
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpRequest
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.translation import ugettext_lazy as _

from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import TokenSerializer, LoginSerializer
from rest_framework import serializers, exceptions, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import User, UserManager, TokenModel, UserFollowing
# from .models import User, UserManager, TokenModel, Follower, Following
from mysite.utils import import_callable

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    follower_num = serializers.IntegerField()
    followee_num = serializers.IntegerField()
    class Meta:
        model = User
        # fields = ('id', 'username', 'email', 'password')
        fields = ('id', 'username', 'email', 'password', 'following', 'followers', 'follower_num', 'followee_num', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}, }

    def get_following(self, obj):
        return UserFollowingSerializer(obj.following.all(), many=True).data
    def get_followers(self, obj):
        return UserFollowersSerializer(obj.followers.all(), many=True).data


class UserEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email',)

class UserProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class UserJoinedSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'date_joined', )


class UserFollowerNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('follower_num', 'followee_num')


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    # def validate(self, data):
    #     if data['password1'] != data['password2']:
    #         raise serializers.ValidationError(_("The two password fields didn't match."))
    #     return data

    def custom_signup(self, request, user):
        # pass
        user.set_password(self.validated_data.get('password'))
        user.save()

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])

        

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'}, required=True)

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    # def _validate_email(self, email, password):
    #     user = None

    #     if email and password:
    #         user = self.authenticate(email=email, password=password)
    #     else:
    #         msg = _('Must include "email" and "password".')
    #         raise exceptions.ValidationError(msg)

        return user

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    # def _validate_username_email(self, username, email, password):
    #     user = None

    #     if email and password:
    #         user = self.authenticate(email=email, password=password)
    #     elif username and password:
    #         user = self.authenticate(username=username, password=password)
    #     else:
    #         msg = _('Must include either "username" or "email" and "password".')
    #         raise exceptions.ValidationError(msg)

    #     return user

    def validate(self, attrs):
        username = attrs.get('username')
        # email = attrs.get('email')
        password = attrs.get('password')

        user = None

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings

            # Authentication through email
            # if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:
            #     user = self._validate_email(email, password)

            # Authentication through username
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
                user = self._validate_username(username, password)

            # Authentication through either username or email
            # else:
            #     user = self._validate_username_email(username, email, password)

        else:
            # Authentication without using allauth
            if email:
                try:
                    username = User.objects.get(email__iexact=email).get_username()
                except User.DoesNotExist:
                    pass

            # if username:
            #     user = self._validate_username_email(username, '', password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    raise serializers.ValidationError(_('E-mail is not verified.'))

        attrs['user'] = user
        return attrs


class UserFollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = '__all__'


class UserFollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("id", "user_id", "created")



class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = TokenModel
        fields = ('key',)


class InfoSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=30)

    def validate(self, data):
        email = data.get("email", None)
        username = data.get("username", None)
        user = User.objects.get(email=email)

        if user is None:
            return {
                'email': 'None'
            }

        return {
            'email': user.email,
            'username': user.username,
        }

class ProfileEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email')




class deleteSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    class Meta:
       model = User