from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from default_web import views
from django.contrib.auth.models import User
from rest_framework import serializers

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'selfservice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^restapi/', include('restapi.urls')),

    url(r'^$', views.index, name='home'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^member/$', views.member_service),
    url(r'^default_web/', include('default_web.urls')),
    url(r'^asia-media-guide/', include('asia_media_guide.urls')),
    url(r'^member_service/', include('member_service.urls')),
    url(r'^asia-media-planning/',include('asia_media_planning.urls')),

    url(r'^accounts/login/$', 'selfservice.views.login'),
    url(r'^accounts/auth/$', 'selfservice.views.auth_view'),
    url(r'^accounts/logout/$', 'selfservice.views.logout'),
    url(r'^accounts/loggedin/$', 'selfservice.views.loggedin'),
    url(r'^accounts/invalid/$', 'selfservice.views.invalid_login'),
    url(r'^accounts/register/$', 'selfservice.views.register_user'),
    url(r'^accounts/register_success/$', 'selfservice.views.register_success'),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )


