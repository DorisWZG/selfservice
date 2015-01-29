from budget_allocation import views
from django.conf.urls import patterns, url
from urlparse import urlparse


urlpatterns = patterns('',

	url(r'^stage2_test/$', views.budget_allocation_test, name='stage2_test'),
	url(r'^stage2_result/industry/(?P<industry>.+)/subindustry/(?P<sub_industry>.+)/budget/(?P<budget>.+)/?$', views.stage2_result, name='stage2_result'),

    url(r'channel_list/$', 'budget_allocation.views.channel_list', name='channel_list'),
    url(r'rest/industry_list/$', 'budget_allocation.views.industry_list', name='industry_list'),
    url(r'get_industryNameList/$', 'budget_allocation.views.get_industryNameList', name='get_industryNameList'),

    url(r'get_subIndustryList/industry/(?P<industry>.+)/?$', 'budget_allocation.views.get_subIndustryList', name='get_subIndustryList'),
    url(r'get_subIndustryList/$', 'budget_allocation.views.get_subIndustryList', name='get_subIndustryList'),

    url(r'rest/metrics_list/$', 'budget_allocation.views.metrics_list', name='metrics_list'),
    url(r'industry_detail/(?P<pk>[0-9])$', 'budget_allocation.views.industry_detail', name='industry_detail'),
    url(r'metrics_list/industry/(?P<industry>.+)/budget/(?P<budget>.+)/?$', 'budget_allocation.views.metrics_list', name='metrics_list'),
    url(r'rest/industry/(?P<industry>.+)/subindustry/(?P<sub_industry>.+)/budget/(?P<budget>.+)/?$', 'budget_allocation.views.metrics_result', name='metrics_result'),
)
