from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import TokenSerializer, LoginSerializer
from django.contrib.auth import password_validation
from .models import User, UserManager, Profile, ProfileStatus
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', )
        extra_kwargs = {'password': {'write_only': True}, }


class UserRegistrationSerializer(RegisterSerializer):
    
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile(user=user, username=validated_data['username'],)
        profile.save()
        return user

class UserLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'}, required=True)
    
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = None
        print(attrs)
        return attrs


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
            # 'token': jwt_token
        }

class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileStatusSerializer(serializers.ModelSerializer):

    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = '__all__'


class UpdateUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'profile',)
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        if profile_data is not None:
            instance.profile.profile_img = profile_data['profile_img']
            instance.profile.user_region = profile_data['user_region']
            instance.profile.group = profile_data['group']
            instance.profile.bio = profile_data['bio']
            instance.profile.sns_name = profile_data['sns_name']
            instance.profile.sns_url = profile_data['sns_url']
            instance.profile.tech_stack = profile_data['tech_stack']
            instance.profile.project_name = profile_data['project_name']
            instance.profile.project_url = profile_data['project_url']
            instance.profile.tag = profile_data['tag']
            instance.profile.save()
        return super().update(instance, validated_data)


class deleteSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    class Meta:
       model = User