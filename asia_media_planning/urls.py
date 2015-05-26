from asia_media_planning import views
from django.conf.urls import patterns, url
from urlparse import urlparse


urlpatterns = patterns('',

	url(r'^china-media/$', views.budget_allocation_test, name='china_media'),
	# url(r'^stage2_result/industry/(?P<industry>.+)/subindustry/(?P<sub_industry>.+)/budget/(?P<budget>.+)/?$', views.stage2_result, name='stage2_result'),

    url(r'^china_media_result/(?P<industry>.+)/(?P<sub_industry>.+)/?$', views.recomm_channels, name='recomm_channels'),

    url(r'channel_list/$', 'asia_media_planning.views.channel_list', name='channel_list'),
    url(r'rest/industry_list/$', 'asia_media_planning.views.industry_list', name='industry_list'),
    url(r'get_industryNameList/$', 'asia_media_planning.views.get_industryNameList', name='get_industryNameList'),

    url(r'get_subIndustryList/industry/(?P<industry>.+)/?$', 'asia_media_planning.views.get_subIndustryList', name='get_subIndustryList'),
    url(r'get_subIndustryList/$', 'asia_media_planning.views.get_subIndustryList', name='get_subIndustryList'),

    url(r'rest/metrics_list/$', 'asia_media_planning.views.metrics_list', name='metrics_list'),
    url(r'industry_detail/(?P<pk>[0-9])$', 'asia_media_planning.views.industry_detail', name='industry_detail'),
    url(r'metrics_list/industry/(?P<industry>.+)/budget/(?P<budget>.+)/?$', 'asia_media_planning.views.metrics_list', name='metrics_list'),
    url(r'rest/industry/(?P<industry>.+)/subindustry/(?P<sub_industry>.+)/budget/(?P<budget>.+)/?$', 'asia_media_planning.views.metrics_result', name='metrics_result'),
)
