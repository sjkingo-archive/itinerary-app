from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'transit.views.overview', name='overview'),
    url(r'^activity/(\d+)/$', 'transit.views.activity', name='activity'),
    url(r'^activity/(\d+)/set_route_index/$', 'transit.views.set_route_index', name='set_route_index'),
)
