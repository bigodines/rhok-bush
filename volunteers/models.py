from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=255)
    where = models.CharField(max_length=255)
    radius = models.CharField(max_length=255)
    skills = models.ManyToManyField('Skill')
    resources = models.ManyToManyField('Resource')

class Call(models.Model):
    title = models.CharField(max_length=255)
    where = models.CharField(max_length=255)
    when = models.DateTimeField()
    classification = models.CharField(max_length=255)
    description = models.TextField()
    skills_needed = models.ManyToManyField('Skill')
    resources_needed = models.ManyToManyField('Resource')

class Skill(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

class Resource(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
