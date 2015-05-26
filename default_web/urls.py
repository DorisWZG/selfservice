from django.conf.urls import patterns, url
from default_web import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^product_and_service/$', views.product_and_service, name='product_and_service'),
	url(r'^education_case/$', views.education_case, name='education_case'),
	url(r'^destination_mkt_case/$', views.destination_mkt_case, name='destination_mkt_case'),
	url(r'^real_estate_case/$', views.real_estate_case, name='real_estate_case'),
	url(r'^high_tech_case/$', views.high_tech_case, name='high_tech_case'),
    url(r'^testimonials.html', views.testimonials, name='testimonials'),

	url(r'^stage1/$', views.stage1, name='stage1'),
    url(r'^getCat1/.*$', views.getCat1, name = 'getCat1'),
    url(r'^getCat2/(?P<cat1>.+)?$', views.getCat2, name = 'getCat2'),
    url(r'^getCat3/(?P<cat2>.+)?$', views.getCat3, name = 'getCat3'),

	# url(r'^stage2_test/$', views.budget_allocation_test, name='stage2_test'),
	# url(r'^stage2_result/$', views.stage2_result, name='stage2_result'),

	url(r'^stage3_test/$', views.wave_test, name='stage3_test'),
	url(r'^stage3_result/$', views.stage3_result, name='stage3_result'),
)
