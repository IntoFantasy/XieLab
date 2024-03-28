from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}.{1}'.format(instance.title, ext)
    return filename


class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    preview_image = models.ImageField('image', upload_to=user_directory_path, blank=True, null=True)
    date = models.DateTimeField("date", default=timezone.now)
    abstract = models.TextField()

    def __str__(self):
        return self.title
