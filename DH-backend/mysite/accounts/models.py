from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
# Create your models here.

# 계정 생성시 반드시 아래의 클래스를 통한다.
class UserManager(BaseUserManager):
    # 일반 사용자 계정을 만들 때 적용되는 함수
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('반드시 이메일 주소를 포함해야합니다.')
        if not username: 
            raise ValueError('반드시 사용자 이름을 포함해야합니다.')
        user = self.model(
            email=self.normalize_email(email),
            username=username 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 슈퍼계정을 만들 때 적용되는 함수
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            password=password,
            username=username
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email        = models.EmailField('email', max_length=60, unique=True)
    username     = models.CharField(max_length=20, unique=True)
    data_joined  = models.DateTimeField('data joined', auto_now_add=True)
    last_login   = models.DateTimeField('last login', auto_now=True)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    # TODO: 프로필 이미지도 추가할 것

    # email을 고유 id로 설정
    USERNAME_FIELD = 'email'
    # 슈퍼계정 생성시 username도 요구하도록 설정
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name ="사용자"
        verbose_name_plural ="사용자"

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    

# 토큰 생성
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)