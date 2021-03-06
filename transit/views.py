import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_POST
import itertools

from models import *

def overview(req, template='overview.html'):
    activities = Activity.objects.order_by('date', 'begins', 'name')
    groups = itertools.groupby(activities, lambda x: x.date)
    a = []
    for date, items in groups:
        # Filter out any non-visible activities. This also implicitly fixes
        # an issue with the template engine failing to iterate over the
        # itertools._grouper (items) by copying it as a list.
        visible_items = [i for i in items if not i.hidden]
        if len(visible_items) > 0:
            a.append((date, visible_items))
    return render(req, template, {
        'groups': a
    })

def activity(req, activity_id, template='activity.html'):
    activity = get_object_or_404(Activity, id=activity_id)
    if activity.hidden:
        raise Http404
    route_to = activity.neighbours[0] and activity.transport_mode != 'DISABLE'
    context = {'activity': activity,
               'prev': activity.neighbours[0],
               'next': activity.neighbours[2],
               'route_to': route_to,
    }
    return render(req, template, context)

@require_POST
def set_route_index(req, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if req.POST:
        activity.route_index = int(req.POST.get('route_index'))
        activity.save()
        return HttpResponse(status=204) # no content
