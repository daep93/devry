from django.db import models
from accounts.models import User
from profiles.models import Profile
from django.conf import settings
from multiselectfield import MultiSelectField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


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

type = (
    ('Conference', 'Conference'),
    ('Workshop', 'Workshop'),
    ('Hackathon', 'Hackathon'),
    ('competition', 'competition'),
    ('Meeting','Meeting'),
)

ch = (
    ('Ready', 'Ready'),
    ('Start', 'Start'),
    ('End', 'End'),
)

class Event(models.Model):
    state= MultiSelectField(max_length=20, choices=ch)
    thumnail = models.ImageField(upload_to="%Y/%m/%d", default="")
    title = models.CharField(max_length=70)
    category = MultiSelectField(choices=type)
    place = models.CharField(max_length=70, default="")
    start = models.DateTimeField()
    end = models.DateTimeField()
    start_day = models.DateField()
    end_day = models.DateField()
    cost = models.CharField(max_length=50, default="")
    participation = models.CharField(max_length=50, default="")
    introduction = models.TextField(default="")
    schedule = models.TextField(default="")
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='event_host')
    ref_tags = MultiSelectField(choices=tech)
    bookmark_num = models.PositiveIntegerField(default=0)
    bookmark_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='bookmark_evnets')
    bookmarked = models.BooleanField(default="False")
    viewed_num = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title