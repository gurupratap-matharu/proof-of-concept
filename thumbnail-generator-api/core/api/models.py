from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

class Profile(models.Model):
    # user = models.OneToOneField('auth.User')
    photo = ThumbnailerImageField(upload_to='photos', blank=True)