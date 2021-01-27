from django.db import models
from accounts.models import User


class Qna(models.Model):
    image = models.ImageField(upload_to="%Y/%m/%d" ,default="")
    title = models.CharField(max_length=30)
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Ans(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    qna = models.ForeignKey(Qna, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)