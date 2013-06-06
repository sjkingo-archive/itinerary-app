from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'transit.views.list_itinerary', name='list_itinerary'),
    url(r'^(\d{4}-\d{2}-\d{2})/$', 'transit.views.day_itinerary', name='day_itinerary'),
)
