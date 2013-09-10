from django.conf.urls import patterns,  url



urlpatterns = patterns('reminder.views',
	url(r'^$', 'index', name='index'),
	url(r'^add_friend$', 'add_friend', name='add_friend'),
	url(r'^add_friend/add$', 'add_friend_add', name='add_friend_add'),
    # Examples:
    # url(r'^$', 'kit.views.home', name='home'),
    # url(r'^kit/', include('kit.foo.urls')),
)
