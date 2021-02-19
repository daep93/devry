from django.db import models
from accounts.models import User, Mentioned
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

class ImagePost(models.Model):
    image = models.ImageField(upload_to="%Y/%m/%d")


class Post(models.Model): 
    title = models.CharField(max_length=80)
    ref_tags = MultiSelectField(choices=tech)
    like_num = models.PositiveIntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    liked = models.BooleanField(default="False")
    bookmark_num = models.PositiveIntegerField(default=0)
    bookmark_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark_posts')
    bookmarked = models.BooleanField(default="False")
    pinned_num = models.PositiveIntegerField(default=0)
    pinned_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='pinned_posts')
    pinned = models.BooleanField(default="False")
    viewed_num = models.PositiveIntegerField(default=0)
    post_num = models.PositiveIntegerField(default=0)
    written_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    writer_info = models.ManyToManyField(Profile, blank=True, related_name='post_profile')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum_post = models.ManyToManyField('self', blank=True, related_name='post_forum_post')
    comments = models.TextField(blank=True)
    comment_num = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField(default="", max_length=100, blank=True, null=False)
    user_info = models.ManyToManyField(Profile, blank=True, related_name='post_userinfo')
    feed_list = models.ManyToManyField('self', blank=True, related_name='post_feed_list')
    recommend_list = models.ManyToManyField('self', blank=True, related_name='post_recommend_list')
    is_following = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='post_profiles')

    def __str__(self):
        return self.title



class Comment(models.Model):
    comment_content = models.TextField()
    assisted = models.BooleanField(default="False")
    like_comment_num = models.PositiveIntegerField(default=0)
    like_comment_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    liked_comment = models.BooleanField(default="False")
    written_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='comments_profile')
    profile_img = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.TextField()
    user_info = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='comments_userinfo')
    mentioned = models.ManyToManyField(Mentioned, blank=True, related_name='comment_mention')

    def __str__(self):
        return self.comment_content




