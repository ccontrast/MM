# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bio'
        db.create_table('myapp_bio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('biography', self.gf('django.db.models.fields.CharField')(max_length=160)),
        ))
        db.send_create_signal('myapp', ['Bio'])


    def backwards(self, orm):
        # Deleting model 'Bio'
        db.delete_table('myapp_bio')


    models = {
        'myapp.bio': {
            'Meta': {'object_name': 'Bio'},
            'biography': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['myapp']