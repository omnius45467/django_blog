from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import BlogPost, HomePage, HomeImage


class HomeView(generic.ListView):
    template_name = "home.html"
    context_object_data = "blog_post"

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['blog_post'] = BlogPost.objects.all()
        ctx['home_page'] = HomePage.objects.all()
        ctx['home_image'] = HomeImage.objects.all()
        return ctx

    def get_queryset(self):
        return BlogPost.objects.filter()


class IndexView(generic.ListView):
   template_name = "blog.html"
   # context_object_name = "latest_blog_post_list"

   def get_context_data(self, **kwargs):
       ctx = super(IndexView, self).get_context_data(**kwargs)
       ctx['blog_post'] = BlogPost.objects.all()
       ctx['home_page'] = HomePage.objects.all()
       ctx['home_image'] = HomeImage.objects.all()
       return ctx

   # def get_queryset(self):
   #     return BlogPost.objects.filter()


class DetailView(generic.DetailView):
   model = BlogPost
   context_object_name="post"
   template_name = "single.html"

   def get_queryset(self):
       """
       Excludes any posts that aren't published yet.
       """
       return BlogPost.objects.filter()