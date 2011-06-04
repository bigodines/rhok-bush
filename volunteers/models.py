from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=255, blank=True)
    where = models.CharField(max_length=255)
    radius = models.CharField(max_length=255, default='1 KM')
    skills = models.ManyToManyField('Skill', blank=True)
    resources = models.ManyToManyField('Resource', blank=True)

    def __unicode__(self):
        return self.name

class Call(models.Model):
    title = models.CharField(max_length=255)
    where = models.CharField(max_length=255)
    when = models.DateTimeField()
    classification = models.CharField(max_length=255)
    description = models.TextField()
    skills_needed = models.ManyToManyField('Skill', blank=True)
    resources_needed = models.ManyToManyField('Resource', blank=True)

    def __unicode__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name
