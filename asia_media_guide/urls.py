from django.conf.urls import patterns, url

from asia_media_guide import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'))