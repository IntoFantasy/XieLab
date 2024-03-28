from django.db import models


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}.{1}'.format(instance.name, ext)
    return filename


class Person(models.Model):
    name = models.CharField(max_length=100)
    position_choice = (
        ("0", "Principal Investigator"),
        ("1", "Researchers"),
        ("2", "PhD. Candidates"),
        ("3", "Master’s Students"),
        ("4", "Undergraduate Students")
    )
    position = models.CharField(max_length=100, choices=position_choice, default="Secret")
    education = models.TextField(max_length=200)
    photo = models.ImageField('photo', upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name
