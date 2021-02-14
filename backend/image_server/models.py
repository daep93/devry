from urllib import request
import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed, post_delete, pre_delete
# from django.core.files import File
# from django.core.files.temp import NamedTemporaryFile
# Create your models here.


class QnaValidate(models.Model):
    qna_image = models.ImageField(upload_to="image_qna/%Y/%m/%d")
    qna_url = models.URLField(max_length=200)

def get_remote_image(self):
    if self.qna.url and not self.qna_image:
        result = urllib.urlretrieve(self, qna_url)
        self.qna_image.save(
            os.path.basename(self.qna_url),
            File(open(result[0]))
        )
        self.save()

class AnsValidate(models.Model):
    ans_image = models.ImageField(upload_to="image_ans/%Y/%m/%d")
    ans_url = models.URLField(max_length=200)

def get_remote_image(self):
    if self.ans.url and not self.ans_image:
        result = urllib.urlretrieve(self, ans_url)
        self.ans_image.save(
            os.path.basename(self.ans_url),
            File(open(result[0]))
        )
        self.save()
