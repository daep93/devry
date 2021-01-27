from django.db import models
from accounts.models import User


class Event(models.Model):
    image = models.ImageField(upload_to="%Y/%m/%d", default="")
    title = models.CharField(max_length=30)
    sdata = models.DateField() # event start date
    stime = models.TimeField()
    edata = models.DateField() # event end date
    etime = models.TimeField()
    location = models.CharField(max_length=30)
    like = models.PositiveIntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    cost = models.CharField(max_length=30, default="")
    target = models.CharField(max_length=30, default="")
    introduction = models.TextField(default="")
    schedule = models.TextField(default="")
    hostinfo = models.TextField(default="")
    tag = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
