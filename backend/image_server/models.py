from urllib import request
import os
from django.db import models
# from django.core.files import File
# from django.core.files.temp import NamedTemporaryFile
# Create your models here.


class QnaValidate(models.Model):
    qna_image = models.ImageField(upload_to="image_qna/%Y/%m/%d")
    qna_url = models.URLField(max_length=200)

# def get_remote_image(self):
#     if self.qna.url and not self.qna_image:
#         result = urllib.urlretrieve(self, qna_url)
#         self.qna_image.save(
#             os.path.basename(self.qna_url),
#             File(open(result[0]))
#         )
#         self.save()
