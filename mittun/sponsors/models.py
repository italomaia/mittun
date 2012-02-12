from django.db import models


class Sponsor(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='sponsors')
