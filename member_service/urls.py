from django.conf.urls import patterns, url
# from default_web import views
from member_service import views


urlpatterns = patterns('',
	url(r'^$', views.ssp_search, name='index'),
	url(r'^ssp_search/$', views.ssp_search, name='ssp_search'),
	url(r'^sales_signal_processing/$', views.sales_signal_processing, name='sales_signal_processing'),
	url(r'^wave/$', views.wave, name='wave'),
	url(r'^endu/$', views.endu, name='endu'),
	url(r'^twins/$', views.twins, name='twins'),
	url(r'base_test/$', views.base_test, name='test'),

    url(r'^sales_opportunities/$', views.sales_opportunities, name='sales_opportunities'),
    url(r'^subscriber_contact/.*$', views.subscriber_contact, name='subscriber_contact'),
    url(r'^getCat1/.*$', views.getCat1, name = 'getCat1'),
    url(r'^getCat2/(?P<cat1>.+)?$', views.getCat2, name = 'getCat2'),
    url(r'^getCat3/(?P<cat2>.+)?$', views.getCat3, name = 'getCat3'),
)
