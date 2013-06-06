import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_POST

from models import *

def list_dates(req, template='list_dates.html'):
    dates = [datetime.date(d.year, d.month, d.day) 
            for d in Activity.objects.dates('date', 'day')]
    return render(req, template, {
        'dates': dates
    })

def daily_itinerary(req, this_date, template='daily_itinerary.html'):
    activities = get_list_or_404(Activity, date=this_date)
    context = {'activities': activities,
               'this_date': activities[0].date} # use a datetime object instead of str
    return render(req, template, context)

@require_POST
def set_route_index(req):
    if req.POST:
        activity_id = req.POST.get('id')
        activity = get_object_or_404(Activity, id=activity_id)
        # update the new route index
        new_route_index = int(req.POST.get('route_index'))
        activity.route_index = new_route_index
        activity.save()
        # return a "No Content" response
        return HttpResponse(status=204)
