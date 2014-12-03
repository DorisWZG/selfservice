from django.conf.urls import patterns, url


urlpatterns = patterns('',
    'restapi.views',
    url(r'^tasks/$', 'task_list', name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),
)
