from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'reminder.views.index'),
	url(r'^reminder/add_friend$', 'reminder.views.add_friend'),
	url(r'^reminder/add_event$', 'reminder.views.add_event'),
    # Examples:
    # url(r'^$', 'kit.views.home', name='home'),
    # url(r'^kit/', include('kit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
