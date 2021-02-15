from django.db import models
from accounts.models import User
from profiles.models import Profile
from django.conf import settings
from multiselectfield import MultiSelectField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from urllib.parse import urlparse
from django.core.files import File
from mysite.utils import download, get_buffer_ext 
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

tags = (
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
    
class Qna(models.Model): 
    title = models.CharField(max_length=70)
    # img=models.ImageField(upload_to="%Y/%m/%d", default="", null=True)
    ref_tags = MultiSelectField(choices=tech)
    like_num = models.PositiveIntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_qnas')
    liked = models.BooleanField(default="False")
    bookmark_num = models.PositiveIntegerField(default=0)
    bookmark_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark_qnas')
    bookmarked = models.BooleanField(default="False")
    pinned_num = models.PositiveIntegerField(default=0)
    pinned_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='pinned_qnas')
    pinned = models.BooleanField(default="False")
    solved=models.BooleanField(default="False")
    viewed_num = models.PositiveIntegerField(default=0)
    written_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='qna_profile')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_info = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, related_name='qna_userinfo')
    is_following = models.BooleanField(default="False")

    def __str__(self):
        return self.title


class Qnasmall(models.Model): 
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    written_time = models.DateTimeField(auto_now_add=True)
    qna = models.ForeignKey(Qna, on_delete=models.CASCADE)
    

class Ans(models.Model):
    content = models.TextField()
    # img = models.ImageField(upload_to="%Y/%m/%d", default="", null="True")
    assist_ans_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='assist_anss')
    assisted = models.BooleanField(default="False")
    like_ans_num = models.PositiveIntegerField(default=0)
    like_ans_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_anss')
    liked_ans = models.BooleanField(default="False")
    written_time = models.DateTimeField(auto_now_add=True)
    qna = models.ForeignKey(Qna, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='ans_profile')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    user_info = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='ans_userinfo')

    def __str__(self):
        return self.content


class Anssmall(models.Model): 
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    written_time = models.DateTimeField(auto_now_add=True)
    ans = models.ForeignKey(Ans, on_delete=models.CASCADE)

class ImagePost(models.Model):
    image = models.ImageField(upload_to="%Y/%m/%d")

