import datetime
from django.shortcuts import render, get_list_or_404

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
