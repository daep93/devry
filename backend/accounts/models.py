import os

from django.conf import settings
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

from rest_framework.authtoken.models import Token as DefaultTokenModel
from mysite.utils import import_callable

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
    # password = models.CharField('password', max_length=20)
    is_staff = models.BooleanField('is_staff', default=False)
    is_active = models.BooleanField('is_active', default=True)
    date_joined = models.DateTimeField('date_joined', default=timezone.now)
    follower_num = models.PositiveIntegerField(default=0)
    followee_num = models.PositiveIntegerField(default=0)
    mentioned = models.BooleanField(default="False")
    mentioned_comment = models.ManyToManyField('forums.Comment', blank=True, related_name='like_comments')

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


TokenModel = import_callable(
    getattr(settings, 'REST_AUTH_TOKEN_MODEL', DefaultTokenModel))

 
class UserFollowing(models.Model):

    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user','following_user'],  name="unique_followers")
        ]
        

    # def __str__(self):
    #     return f"user_id = {self.user_id} follows user_id = {self.following_user_id}"

class Mentioned(models.Model):

    user = models.ForeignKey(User, related_name="mention_user", on_delete=models.CASCADE)
    mentioned_user = models.ForeignKey(User, related_name="mentioned_user", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # comment = models.ManyToManyField('forums.Comment', blank=True, related_name='mentioned_comment')
    comment = models.ForeignKey('forums.Comment', blank=True, on_delete=models.CASCADE, related_name='mentioned_comment')


