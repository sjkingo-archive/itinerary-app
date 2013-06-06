from django.shortcuts import render, get_list_or_404

from models import *

def list_dates(req, template='list_dates.html'):
    activities = Activity.objects.all()
    dates = set()
    for a in activities:
        dates.add(a.date)
    context = {'dates': dates}
    return render(req, template, context)

def daily_itinerary(req, this_date, template='daily_itinerary.html'):
    activities = get_list_or_404(Activity, date=this_date)
    context = {'activities': activities,
               'this_date': activities[0].date} # use a datetime object instead of str
    return render(req, template, context)
