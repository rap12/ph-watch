# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Office'
        db.create_table('devcup_office', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_no', self.gf('django.db.models.fields.IntegerField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('head', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('gmapsfield.fields.GoogleMapsField')()),
        ))
        db.send_create_signal('devcup', ['Office'])

        # Adding model 'Project'
        db.create_table('devcup_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devcup.Office'])),
            ('contractor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('budget', self.gf('django.db.models.fields.FloatField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('address', self.gf('gmapsfield.fields.GoogleMapsField')()),
        ))
        db.send_create_signal('devcup', ['Project'])


    def backwards(self, orm):
        
        # Deleting model 'Office'
        db.delete_table('devcup_office')

        # Deleting model 'Project'
        db.delete_table('devcup_project')


    models = {
        'devcup.office': {
            'Meta': {'object_name': 'Office'},
            'address': ('gmapsfield.fields.GoogleMapsField', [], {}),
            'contact_no': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'head': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'devcup.project': {
            'Meta': {'object_name': 'Project'},
            'address': ('gmapsfield.fields.GoogleMapsField', [], {}),
            'budget': ('django.db.models.fields.FloatField', [], {}),
            'contractor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devcup.Office']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['devcup']
