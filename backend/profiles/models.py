from django.db import models
from accounts.models import User
from accounts.serializers import UserSerializer
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
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
    ('Frontend', 'Frontend'),
    ('Backend', 'Backend'),
    ('DevOps', 'DevOps'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('BigData', 'BigData'),
    ('Blockchain', 'Blockchain'),
    ('Internet of Things', 'Internet of Things'),
    ('Augmented Reality', 'Augmented Reality'),
    ('Virtual Reality', 'Virtual Reality'),
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
    ('Frontend', 'Frontend'),
    ('Backend', 'Backend'),
    ('DevOps', 'DevOps'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('BigData', 'BigData'),
    ('Blockchain', 'Blockchain'),
    ('Internet of Things', 'Internet of Things'),
    ('Augmented Reality', 'Augmented Reality'),
    ('Virtual Reality', 'Virtual Reality'),
)

# Create your models here.
class ForumImagePost(models.Model):
    thumbnail = models.ImageField(upload_to="%Y/%m/%d") 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    follower_num = models.PositiveIntegerField(default=0)
    followee_num = models.PositiveIntegerField(default=0)    
    profile_img = models.URLField(default="", max_length=100, blank=True, null=False)

    region = models.CharField(max_length=100, blank=True)
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
    my_tags = MultiSelectField(choices=user_tag)
    pinned_qnas = models.TextField(blank=True)
    pinned_forums = models.TextField(blank=True)
    qnas = models.TextField(blank=True)
    forums = models.TextField(blank=True)
    qnas_comments = models.TextField(blank=True)
    forums_comments = models.TextField(blank=True)
    link = models.ManyToManyField('self', default = 0, related_name='project_link', blank=True)
    links = models.TextField()
    project = models.ManyToManyField('self', default = 0, related_name='project_project', blank=True)
    projects = models.TextField()
    thumbnail = models.OneToOneField(ForumImagePost, on_delete=models.CASCADE, blank=True, null=True, related_name='forum_image')
    is_following = models.BooleanField(default=False)
    joined = models.DateTimeField(blank=True, null=True)
    tags = models.TextField(blank=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
    instance.profile.username = UserSerializer(instance).data['username']
    instance.profile.email = UserSerializer(instance).data['email']
    instance.profile.joined = UserSerializer(instance).data['date_joined']
    instance.profile.save()

