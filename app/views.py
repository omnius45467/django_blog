from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import BlogPost
class IndexView(generic.ListView):
   template_name = "index.html"
   context_object_name = "latest_blog_post_list"

   def get_queryset(self):
       return BlogPost.objects.filter()

class DetailView(generic.DetailView):
   model = BlogPost
   context_object_name="post"
   template_name = "detail.html"

   def get_queryset(self):
       """
       Excludes any posts that aren't published yet.
       """
       return BlogPost.objects.filter()
