TODO
====

* add `arrival_time` field that differs from `begins` (Maps will use
  `arrival_time` instead when routing)
* group fields in admin using [fieldsets](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets)
* mobile stylesheet (single column)
* print stylesheet
* display info message when `set_route_index` is called
* fix style when no directions are displayed
* [grapelli](https://github.com/sehmaschine/django-grappelli) admin skin?
* `transit/models.py:neighbours()`: stop iterating over the list each time
* allow activities to span multiple days
* add time zone support instead of assuming one time zone
