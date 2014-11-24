from django.conf.urls import patterns, url
# from default_web import views
from member_service import views


urlpatterns = patterns('',
	# url(r'^$', views.index, name='index'),
	url(r'^sales_signal_processing/$', views.sales_signal_processing, name='sales_signal_processing'),
	url(r'^wave/$', views.wave, name='wave'),
	url(r'^endu/$', views.endu, name='endu'),
	url(r'^twins/$', views.twins, name='twins'),
	url(r'base_test/$', views.base_test, name='test'),
)
