import os

from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}.{1}'.format(instance.title, ext)
    return filename


class Publication(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    preview_image = models.ImageField('preview', upload_to=user_directory_path, blank=True, null=True)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    pub_year = models.PositiveIntegerField(default=1999)

    def __str__(self):
        return self.title
