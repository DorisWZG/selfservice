from django.conf.urls import patterns, url
from urlparse import urlparse
from asia_media_guide import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'))