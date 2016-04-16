from django.contrib import admin

from .models import BlogPost #this line added
admin.site.register(BlogPost)#this line added

