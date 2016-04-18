from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import BlogPost, HomeImage, HomePage, AuthorBio #this line added


class BlogPostAdmin(admin.ModelAdmin):
    admin.site.register(BlogPost, SummernoteModelAdmin)#this line added


class HomePageAdmin(admin.ModelAdmin):
    admin.site.register(HomePage, SummernoteModelAdmin)#this line added


class HomeImageAdmin(admin.ModelAdmin):
    admin.site.register(HomeImage, SummernoteModelAdmin)  # this line added

class AuthorBioAdmin(admin.ModelAdmin):
    admin.site.register(AuthorBio, SummernoteModelAdmin)