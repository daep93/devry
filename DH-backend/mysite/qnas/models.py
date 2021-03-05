from django.db import models

# Create your models here.


class Qna(models.Model): 
    title = models.CharField(max_length=70)
    content = models.TextField('Content', default='')
    written_time = models.DateTimeField(auto_now=True)
    ref_tags = models.TextField('Ref Tags', default='')
    writer = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, verbose_name="작성자") 
    viewed_num = models.PositiveIntegerField(default=0)
    solved = models.BooleanField(default="False")
    
    def __str__(self):
        return self.title

# class Comment(models.Model):
#     user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='사용자')
#     qna = models.ForeignKey('Qna', on_delete=models.CASCADE, verbose_name='QnA 번호')
#     content = models.TextField('Content', default='')

# class Like(models.Model):
#     user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='사용자')
#     qna = models.ForeignKey('Qna', on_delete=models.CASCADE, verbose_name='QnA 번호')

# class Bookmark(models.Model):
#     user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='사용자')
#     qna = models.ForeignKey('Qna', on_delete=models.CASCADE, verbose_name='QnA 번호')

# class Pin(models.Model):
#     user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='사용자')
#     qna = models.ForeignKey('Qna', on_delete=models.CASCADE, verbose_name='QnA 번호')
