from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import BlogPost #this line added
admin.site.register(BlogPost, SummernoteModelAdmin)#this line added
