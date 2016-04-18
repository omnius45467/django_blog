from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^about/(?P<pk>[0-9]+)$', views.AboutView.as_view(), name='about')
]