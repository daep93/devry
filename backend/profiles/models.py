from django.db import models
from accounts.models import User
from accounts.serializers import UserSerializer
from articles.models import Article, Comment

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from multiselectfield import MultiSelectField

tech = (
    ('PY', 'Python3'),
    ('DJ', 'Django'),
    ('JV', 'Java'),
    ('SP', 'Spring'),
    ('HT', 'HTML5'),
    ('CS', 'CSS3'),
    ('JS', 'JavaScript'),
    ('VU', 'Vue.js'),
    ('RE', 'React'),
    ('AN', 'Angular'),
    ('NO', 'Node.js'),
    ('RU', 'Ruby'),
    ('RO', 'Ruby on Rails'),
    ('MY', 'MySQL'),
    ('MD', 'MariaDB'),
    ('MB', 'MongoDB'),
    ('DK', 'Docker'),
    ('KN', 'Kubernetes'),
)

tags = (
    ('PY', 'Python3'),
    ('DJ', 'Django'),
    ('JV', 'Java'),
    ('SP', 'Spring'),
    ('HT', 'HTML5'),
    ('CS', 'CSS3'),
    ('JS', 'JavaScript'),
    ('VU', 'Vue.js'),
    ('RE', 'React'),
    ('AN', 'Angular'),
    ('NO', 'Node.js'),
    ('RU', 'Ruby'),
    ('RO', 'Ruby on Rails'),
    ('MY', 'MySQL'),
    ('MD', 'MariaDB'),
    ('MB', 'MongoDB'),
    ('DK', 'Docker'),
    ('KN', 'Kubernetes'),
    ('FE', 'FrontEnd'),
    ('BE', 'BackEnd'),
    ('DO', 'DevOps'),
    ('AI', 'Artificial Intelligence'),
    ('BD', 'BigData'),
    ('BC', 'Blockchain'),
    ('IT', 'Internet of Things'),
    ('AR', 'Augmented Reality'),
    ('VR', 'Virtual Reality'),
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    profile_img = ProcessedImageField(
        default="",
        blank = True,
        upload_to = 'accounts/images',
        processors= [ResizeToFill(200, 200)],
        format='JPEG',
        # options= {'quality': 90},
    )
    user_region = (
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
    region = models.CharField(max_length=4, choices=user_region, blank=True)
    group = models.CharField(default="", max_length=40, blank=True)
    bio = models.TextField(default="", blank=True)
    sns_name = models.TextField(default="", blank=True)
    sns_url = models.CharField(default="", max_length=100, blank=True)
    tech_stack = MultiSelectField(choices=tech)
    project_name = models.CharField(default="", max_length=100, blank=True)
    project_url = models.CharField(default="", max_length=100, blank=True)
    tag = MultiSelectField(choices=tags)
    # posts = models.ForeignKey(Article, on_delete=models.CASCADE)
    pinned_posts = models.ManyToManyField(Article, related_name='profile_pinned_posts')
    posts = models.ManyToManyField(Article, related_name='profile_posts')
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, related_name='profile_comments')
    
    def __str__(self):
        return self.username