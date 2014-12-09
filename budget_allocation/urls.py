from budget_allocation import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',

	url(r'^stage2_test/$', views.budget_allocation_test, name='stage2_test'),
	url(r'^stage2_result/$', views.stage2_result, name='stage2_result'),


    url(r'channel_list/$', 'budget_allocation.views.channel_list', name='channel_list'),
    url(r'industry_list/$', 'budget_allocation.views.industry_list', name='industry_list'),
    url(r'metrics_list/$', 'budget_allocation.views.metrics_list', name='metrics_list'),
    url(r'industry_detail/(?P<pk>[0-9])$', 'budget_allocation.views.industry_detail', name='industry_detail'),
    url(r'metrics_list/industry/(?P<industry>.+)/budget/(?P<budget>.+)/?$', 'budget_allocation.views.metrics_list', name='metrics_list'),
    url(r'metrics_result/industry/(?P<industry>.+)/budget/(?P<budget>.+)/?$', 'budget_allocation.views.metrics_result', name='metrics_result'),
)
