from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=30)
    resources = models.ManyToManyField('Resource')

class Resource(models.Model):
    name = models.CharField(max_length=30)

class Event(models.Model):
    name = models.CharField(max_length=30)
    date_time = models.DateTimeField()
    resources_required = models.ManyToManyField('Resource')
