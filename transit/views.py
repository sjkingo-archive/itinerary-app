from django.shortcuts import render, get_list_or_404
import datetime

from models import *

def list_itinerary(req, template='list.html'):
    activities = Activity.objects.all()
    dates = set()
    for a in activities:
        dates.add(a.date)
    context = {'dates': dates}
    return render(req, template, context)

def day_itinerary(req, date, template='day.html'):
    activities = get_list_or_404(Activity, date=date)
    #activities = zip(r[:], r[1:])
    context = {'activities': activities,
               'date': date}
    return render(req, template, context)
