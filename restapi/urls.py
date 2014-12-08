from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # 'restapi.views',
    # url(r'task_list/$', 'restapi.views.task_list', name='task_list'),
    # url(r'task_detail/(?P<pk>[0-9]+)$', 'restapi.views.task_detail', name='task_detail'),
    url(r'channel_list/$', 'restapi.views.channel_list', name='channel_list'),
    url(r'industry_list/$', 'restapi.views.industry_list', name='industry_list'),
    url(r'industry_detail/(?P<pk>[0-9])$', 'restapi.views.industry_detail', name='industry_detail'),
    # url(r'budget_list/$', 'restapi.views.budget_list', name='budget_list'),
    url(r'matrix_list/industry/(?P<industry>.+)/budget/(?P<budget>.+)/?$', 'restapi.views.matrix_list', name='matrix_list'),
)
