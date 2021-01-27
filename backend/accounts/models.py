import os

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from django.dispatch import receiver
from django.urls import reverse
from django.template.loader import render_to_string
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from django.db.models.signals import post_save
from django.dispatch import receiver

from multiselectfield import MultiSelectField
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields): 
        if not email:
            raise ValueError('input email')
        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True or extra_fields.get('is_superuser') is not True:
            raise ValueError('not Superuser')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', max_length=80, unique=True)
    username = models.CharField('username', max_length=30, unique=True)
    is_staff = models.BooleanField('is_staff', default=False)
    is_active = models.BooleanField('is_active', default=True)
    date_joined = models.DateTimeField('date_joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
    def __str__(self):
        return self.username

    # email = models.EmailField('email', unique=True)
    # username = models.CharField(max_length=20, unique=True)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute.uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    }

    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_pk = models.IntegerField(blank=True)
    # email = models.EmailField(max_length=500, unique=True)
    username = models.CharField(max_length=20)
    profile_img = ProcessedImageField(
        blank = True,
        upload_to = 'accounts/images',
        processors= [ResizeToFill(150, 150)],
        format='JPEG',
        options= {'quality': 90},
    )
    REGION = (
        ('SEL', '서울'),
        ('PUS', '부산'),
        ('TAE', '대구'),
        ('INC', '인천'),
        ('KWJ', '광주'),
        ('TAJ', '대전'),
        ('USN', '울산'),
        ('KYG', '경기'),
        ('KAW', '강원'),
        ('CCB', '충북'),
        ('CCN', '충남'),
        ('CLB', '전북'),
        ('CLN', '전남'),
        ('KSB', '경북'),
        ('KSN', '경남'),
        ('CHJ', '제주')
    )
    user_region = models.CharField(max_length=4, choices=REGION, blank=True)
    group = models.CharField(max_length=40, blank=True)
    bio = models.TextField(blank=True)
    sns_name = models.TextField(blank=True)
    sns_url = models.URLField(blank=True)
    tech = (
        ('PY', 'Python3'),
        ('JV', 'Java'),
        ('HT', 'HTML5'),
        ('CS', 'CSS3'),
        ('JS', 'JavaScript'),
        ('VU', 'Vue.js'),
        ('RE', 'React.js'),
        ('AN', 'Angular'),
        ('MY', 'MySQL'),
        ('MD', 'MariaDB'),
    )
    tech_stack = MultiSelectField(choices=tech)
    project_name = models.CharField(max_length=100, blank=True)
    project_url = models.URLField(blank=True)
    tag = models.CharField(max_length=20, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Profile.objects.create(user=instance, user_pk=instance.id)
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # status_content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses"
    
    def __str__(self):
        return str(self.user_profile)
    