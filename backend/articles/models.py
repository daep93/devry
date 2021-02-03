from django.db import models
from accounts.models import User
from django.conf import settings
from multiselectfield import MultiSelectField


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
    
class Article(models.Model): 
    title = models.CharField(max_length=30)
    thumbnail_img = models.ImageField(upload_to="%Y/%m/%d", default="")   
    ref_tags = MultiSelectField(choices=tech)
    like_num = models.PositiveIntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    liked = models.BooleanField(default="True")
    bookmark_num = models.PositiveIntegerField(default=0)
    bookmark_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark_articles')
    bookmarked= models.BooleanField(default="True")
    # bio = models.TextField()
    viewed_num = models.PositiveIntegerField(default=0)
    written_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # username =models.CharField(default="")
    content = models.TextField()
    profile_img=models.ImageField(upload_to="%Y/%m/%d", default="")
    

class Comment(models.Model):
    comment_content = models.TextField()
    profile_img=models.ImageField(upload_to="%Y/%m/%d", default="")
    written_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)