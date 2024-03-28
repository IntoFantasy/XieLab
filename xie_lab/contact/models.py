from django.db import models


class Contact(models.Model):
    description = models.TextField(max_length=2000)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()

