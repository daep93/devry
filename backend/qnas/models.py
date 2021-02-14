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


class QnaPicture(models.Model):
    post_image = models.ForeignKey(Qna, on_delete=models.CASCADE)
    image = models.ImageField()


class ImageFile(models.Model):
    # img_file = models.FileField(blank=False, null=False, upload_to='qna')
    img_file = models.ImageField(blank=False, null=False, upload_to='qna')
    description = models.CharField(max_length=255, blank=True)
    img_url = models.URLField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    qna = models.ForeignKey(Qna, null=True, on_delete=models.CASCADE, related_name='qna_image')


    # def __str__(self):
    #     return self.img_file
    def __unicode__(self):
        return os.path.basename(self.img_file.name)

class QnaImageURL(models.Model):
    purchase_url = models.URLField('URL', max_length=400, blank=True)
    image_file = models.ImageField('Image', upload_to='qna', blank=True)

def save(self, *args, **kwargs):
    # ImageField에 파일이 없고, url이 존재하는 경우에만 실행
    if self.purchase_url and not self.image_file:
        # 우선 purchase_url의 대표 이미지를 크롤링하는 로직은 생략하고, 크롤링 결과 이미지 url을 임의대로 설정  
        item_image_url = 'https://cdn.pixabay.com/photo/2016/08/27/11/17/bag-1623898_960_720.jpg'

        if item_image_url:
            temp_file = download(item_image_url)
            file_name = '{urlparse}.{ext}'.format(
                # url의 마지막 '/' 내용 중 확장자 제거
                # ex) url = 'https://~~~~~~/bag-1623898_960_720.jpg'
                #     -> 'bag-1623898_960_720.jpg'
                #     -> 'bag-1623898_960_720'
                urlparse=urlparse(item_image_url).path.split('/')[-1].split('.')[0],
                ext=get_buffer_ext(temp_file)
            )
            self.image_file.save(file_name, File(temp_file))
            super().save()
        else:
            super().save()