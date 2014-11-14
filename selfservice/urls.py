from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from default_web import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'selfservice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', include('default_web.urls')),
    url(r'^$', views.index),
    url(r'^contact/$', views.contact),
    url(r'^about/$', views.about),
    url(r'^member/$', views.member_service),
    url(r'^default_web/', include('default_web.urls')),

)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT ) 


