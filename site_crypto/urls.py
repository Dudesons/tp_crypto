from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site_crypto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'site_crypto.views.home', name='home'),
    url(r'^crypt/$', 'site_crypto.views.home', name='crypt'),
    url(r'^admin/', include(admin.site.urls)),
)
