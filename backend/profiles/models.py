from django.db import models
from accounts.models import User
from accounts.serializers import UserSerializer
from articles.models import Article, Comment
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from multiselectfield import MultiSelectField

tech = (
    ('Python3', 'Python3'),
    ('Django', 'Django'),
    ('Java', 'Java'),
    ('Spring', 'Spring'),
    ('HTML5', 'HTML5'),
    ('CSS3', 'CSS3'),
    ('JavaScript', 'JavaScript'),
    ('TypeScript', 'TypeScript'),
    ('Vue.js', 'Vue.js'),
    ('React', 'React'),
    ('Angular', 'Angular'),
    ('Node.js', 'Node.js'),
    ('Swift', 'Swift'),
    ('Ruby', 'Ruby'),
    ('Ruby on Rails', 'Ruby on Rails'),
    ('MySQL', 'MySQL'),
    ('MariaDB', 'MariaDB'),
    ('MongoDB', 'MongoDB'),
    ('Docker', 'Docker'),
    ('Kubernetes', 'Kubernetes'),
)

user_tag = (
    ('Python3', 'Python3'),
    ('Django', 'Django'),
    ('Java', 'Java'),
    ('Spring', 'Spring'),
    ('HTML5', 'HTML5'),
    ('CSS3', 'CSS3'),
    ('JavaScript', 'JavaScript'),
    ('TypeScript', 'TypeScript'),
    ('Vue.js', 'Vue.js'),
    ('React', 'React'),
    ('Angular', 'Angular'),
    ('Node.js', 'Node.js'),
    ('Swift', 'Swift'),
    ('Ruby', 'Ruby'),
    ('Ruby on Rails', 'Ruby on Rails'),
    ('MySQL', 'MySQL'),
    ('MariaDB', 'MariaDB'),
    ('MongoDB', 'MongoDB'),
    ('Docker', 'Docker'),
    ('Kubernetes', 'Kubernetes'),
    ('FrontEnd', 'FrontEnd'),
    ('BackEnd', 'BackEnd'),
    ('DevOps', 'DevOps'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('BigData', 'BigData'),
    ('Blockchain', 'Blockchain'),
    ('Internet of Things', 'Internet of Things'),
    ('Augmented Reality', 'Augmented Reality'),
    ('Virtual Reality', 'Virtual Reality'),
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    follower_num = models.PositiveIntegerField(default=0)
    followee_num = models.PositiveIntegerField(default=0)    
    profile_img = ProcessedImageField(
        default="",
        blank = True,
        upload_to = 'accounts/images',
        processors= [ResizeToFill(200, 200)],
        format='JPEG',
        # options= {'quality': 90},
    )
    user_region = (
        ('서울', '서울'),
        ('부산', '부산'),
        ('대구', '대구'),
        ('인천', '인천'),
        ('광주', '광주'),
        ('대전', '대전'),
        ('울산', '울산'),
        ('경기', '경기'),
        ('강원', '강원'),
        ('충북', '충북'),
        ('충남', '충남'),
        ('전북', '전북'),
        ('전남', '전남'),
        ('경북', '경북'),
        ('경남', '경남'),
        ('제주', '제주')
    )
    region = models.CharField(max_length=4, choices=user_region, blank=True)
    group = models.CharField(default="", max_length=40, blank=True)
    bio = models.TextField(default="", blank=True)
    sns_name1 = models.TextField(default="", blank=True)
    sns_name2 = models.TextField(default="", blank=True)
    sns_name3 = models.TextField(default="", blank=True)
    sns_url1 = models.URLField(default="", max_length=100, blank=True)
    sns_url2 = models.URLField(default="", max_length=100, blank=True)
    sns_url3 = models.URLField(default="", max_length=100, blank=True)
    tech_stack = MultiSelectField(choices=tech)
    project_name1 = models.CharField(default="", max_length=100, blank=True)
    project_name2 = models.CharField(default="", max_length=100, blank=True)
    project_name3 = models.CharField(default="", max_length=100, blank=True)
    project_url1 = models.URLField(default="", max_length=100, blank=True)
    project_url2 = models.URLField(default="", max_length=100, blank=True)
    project_url3 = models.URLField(default="", max_length=100, blank=True)
    tag = MultiSelectField(choices=user_tag)
    pinned_posts = models.ManyToManyField(Article, related_name='profile_pinned_posts')
    posts = models.ManyToManyField(Article, related_name='profile_posts')
    comments = models.ManyToManyField(Comment, related_name='profile_comments')
    links = models.ManyToManyField('self', default=0 ,related_name='link_sns', blank=True)
    projects = models.ManyToManyField('self', default=0, related_name='project_project', blank=True)
    joined = models.DateTimeField(blank=True)
    tags = models.TextField(blank=True)

