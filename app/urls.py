from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    # ex: /5/
    url(r'^blog/post/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
]