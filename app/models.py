from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from taggit.managers import TaggableManager
from django.db import models


class BlogPost(models.Model):
    image = models.ImageField('img', upload_to='media', default='post.jpg')
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    tags = TaggableManager()

    def __str__(self):              # __unicode__ on Python 2
        return self.title


class HomePage(models.Model):
    title = models.CharField(max_length=100)
    section_1=models.TextField()
    section_2=models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title


class HomeImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField('img', upload_to='media', default='post.jpg')
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title
