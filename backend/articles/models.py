from django.db import models
from accounts.models import User
from django.conf import settings
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
    
class Article(models.Model): 
    title = models.CharField(max_length=30)
    thumbnail_img = models.ImageField(upload_to="%Y/%m/%d", default="")   
    tags = MultiSelectField(choices=tags)
    like_num = models.PositiveIntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    liked = models.BooleanField(default="False")
    bookmark_num = models.PositiveIntegerField(default=0)
    bookmark_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark_articles', blank=True)
    bookmarked= models.BooleanField(default="False")
    # bio = models.TextField()
    viewed_num = models.PositiveIntegerField(default=0)
    written_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # username =models.CharField(default="")
    content = models.TextField()
    profile_img=models.ImageField(upload_to="%Y/%m/%d", default="")
    pinned_num = models.PositiveIntegerField(default=0)
    pinned_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='pinned_articles')
    pinned_post = models.BooleanField(default="False")

class Comment(models.Model):
    comment_content = models.TextField()
    profile_img=models.ImageField(upload_to="%Y/%m/%d", default="")
    written_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_profile_title')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_username')
    # parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)