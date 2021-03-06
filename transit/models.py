from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property

TRANSPORT_MODES = (
    ('DISABLE', 'Disabled'),
    ('DRIVING', 'Driving/Taxi'),
    ('TRANSIT', 'Transit'),
    ('WALKING', 'Walking')
)

class Activity(models.Model):
    date = models.DateField()
    begins = models.TimeField(verbose_name='Begins at')
    ends = models.TimeField(verbose_name='Ends at', blank=True, null=True)

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    notes = models.TextField(blank=True, null=True)

    transport_mode = models.CharField(max_length=10,
            help_text='Mode of transport to get *to* this activity. Set to Disable to prevent it from '
                      'being included in route calculations.',
            choices=TRANSPORT_MODES,
            default='TRANSIT')
    hidden = models.BooleanField(verbose_name='Hidden', 
            help_text='Prevent this activity from being displayed. Note that it will still be used in '
                      'route calculations unless "Transport mode" is set to "Disabled".')
    route_index = models.IntegerField(blank=True, null=True,
            help_text='Optional index of the chosen route to this activity. Click on a suggested route '
                      'on the activity page to automatically set this, and that route will be chosen '
                      'each time the activity is loaded.')

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        ordering = ['date', 'begins', 'name']

    def __unicode__(self):
        return self.name

    @cached_property
    def neighbours(self):
        """
        Returns a triplet (prev, this, next) of this Activity's neighbours.
        Either (or both) prev and next may be None if we are at the either end
        of the chain.

        We cache this result (@cached_property) as it saves database lookups
        and CPU time as it has to iterate over all activities.
        
        FIXME: use activities.index() instead of iterating over?
        """
        activities = Activity.objects.all()
        for n, this_a in enumerate(activities):
            if this_a == self:
                try:
                    prev_a = activities[n-1]
                except (IndexError, AssertionError), e:
                    prev_a = None

                try:
                    next_a = activities[n+1]
                except IndexError:
                    next_a = None

                return (prev_a, this_a, next_a)

    @property
    def reversed_url(self):
        return reverse('activity', args=(self.id,))

    @property
    def to_mode(self):
        return dict(TRANSPORT_MODES)[self.transport_mode]

admin.site.register(Activity)
