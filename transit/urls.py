from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'transit.views.list_dates', name='list_dates'),
    url(r'^(\d{4}-\d{2}-\d{2})/$', 'transit.views.daily_itinerary', name='daily_itinerary'),
)
