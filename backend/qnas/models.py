from django.db import models
from accounts.models import User
from profiles.models import Profile
from django.conf import settings
from multiselectfield import MultiSelectField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

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
    
class Qna(models.Model): 
    title = models.CharField(max_length=30)
    ref_tags = MultiSelectField(choices=tech)
    like_num = models.PositiveIntegerField(default=0)
    comment_num = models.PositiveIntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_qnas')
    liked = models.BooleanField(default="False")
    bookmark_num = models.PositiveIntegerField(default=0)
    bookmark_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark_qnas')
    bookmarked = models.BooleanField(default="False")
    solved=models.BooleanField(default="False")
    viewed_num = models.PositiveIntegerField(default=0)
    written_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title

class Qnasmall(models.Model): 
    content = models.TextField()
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    username =models.CharField(max_length=30, default="")
    written_time = models.DateTimeField(auto_now_add=True)
    qna = models.ForeignKey(Qna, on_delete=models.CASCADE)
    

class Ans(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    assisted = models.BooleanField(default="False")
    like_ans_num = models.PositiveIntegerField(default=0)
    like_ans_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_anss')
    liked_ans = models.BooleanField(default="False")
    written_time = models.DateTimeField(auto_now_add=True)
    qna = models.ForeignKey(Qna, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Anssmall(models.Model): 
    content = models.TextField()
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    username =models.CharField(max_length=30, default="")
    written_time = models.DateTimeField(auto_now_add=True)
    ans = models.ForeignKey(Ans, on_delete=models.CASCADE)
