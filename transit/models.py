from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property

class Activity(models.Model):
    date = models.DateField()
    begins = models.TimeField(verbose_name='Begins at')
    ends = models.TimeField(verbose_name='Ends at')
    hidden = models.BooleanField(verbose_name='Hidden?', 
            help_text='This is typically used on the root entry as it does not have an origin.')

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    notes = models.TextField(blank=True, null=True)
    route_index = models.IntegerField(blank=True, null=True,
            help_text='Optional index of the chosen route to this activity.')

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

    @cached_property
    def reversed_url(self):
        return reverse('activity', args=(self.id,))

admin.site.register(Activity)
