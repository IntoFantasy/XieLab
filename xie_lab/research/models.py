from django.db import models


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}.{1}'.format(instance.direction, ext)
    return filename


class Research(models.Model):
    direction = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField()
    icon = models.ImageField('icon', upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return str(self.order) + ". " + self.direction


class Abstract(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description
