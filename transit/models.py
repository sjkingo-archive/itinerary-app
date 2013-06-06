from django.contrib import admin
from django.db import models

from itinerary.utils import cached_property

class Activity(models.Model):
    date = models.DateField()
    begins = models.TimeField(verbose_name='Begins at')
    ends = models.TimeField(verbose_name='Ends at')

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        ordering = ['date', 'begins', 'name']

    def __unicode__(self):
        return self.name

    @cached_property
    def origin(self):
        """
        Returns the activity before this one.
        """
        # We construct a list here to reduce the number of queries by the
        # number of Activity.objects.count() when we zip the QuerySet's
        # together.
        r = list(Activity.objects.filter(date=self.date).order_by('begins').all())
        pairs = zip(r, r[1:]) #: [(origin, activity), ..]
        for origin, activity in pairs:
            # Find this activity and return its previous activity in the chain
            if activity == self:
                return origin
        # Should never get here but it will break the template rendering if we do
        raise Exception('Could not find an origin for ' + repr(activity))

admin.site.register(Activity)
