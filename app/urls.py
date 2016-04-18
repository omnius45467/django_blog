from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^blog/$', views.BlogView.as_view(), name='detail'),
    url(r'^blog/post/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^blog/tags/(?P<name>[a-zA-Z0-9_.-]+)/$', views.TagView.as_view(), name='tags')

]