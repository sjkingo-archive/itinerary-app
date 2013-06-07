# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Activity.ends'
        db.alter_column(u'transit_activity', 'ends', self.gf('django.db.models.fields.TimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'Activity.ends'
        db.alter_column(u'transit_activity', 'ends', self.gf('django.db.models.fields.TimeField')(default=None))

    models = {
        u'transit.activity': {
            'Meta': {'ordering': "['date', 'begins', 'name']", 'object_name': 'Activity'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'begins': ('django.db.models.fields.TimeField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'ends': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'route_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['transit']