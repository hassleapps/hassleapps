from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hassle_sms.views.home', name='home'),

#    url(r'^admin/', include(admin.site.urls)),

    # Twilio URLs
    url(r'^sms/$', 'hassle_sms.views.sms'),
#    url(r'^ring/$', 'hassle_sms.views.ring'),
)
