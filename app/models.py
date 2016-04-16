from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

from django.db import models

class BlogPost(models.Model):

    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):              # __unicode__ on Python 2
        return self.title

