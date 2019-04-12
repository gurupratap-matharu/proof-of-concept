from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Profile(models.Model):
    """
    Our profile model that holds the images in the database from which
    we make thumbnails.
    """
    photo = ThumbnailerImageField(upload_to='photos', blank=True)
    owner = models.ForeignKey('auth.User', related_name='photos', on_delete=models.CASCADE, blank=True, null=True)
    remark = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
