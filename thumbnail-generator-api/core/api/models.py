from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    photo = ThumbnailerImageField(upload_to='photos', blank=True)
    remark = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
