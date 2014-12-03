from django.conf.urls import patterns, url
from budget_allocation import views


urlpatterns = patterns('',

	url(r'^stage2_test/$', views.budget_allocation_test, name='stage2_test'),
	url(r'^stage2_result/$', views.stage2_result, name='stage2_result'),
)
