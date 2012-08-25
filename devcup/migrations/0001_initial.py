# -*- coding: utf-8 -*-
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
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('contact_no', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('head', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('gmapsfield.fields.GoogleMapsField')(default='{ coordinates: [14.6001, 120.9843], zoom: 10, size: [400, 200] }')),
        ))
        db.send_create_signal('devcup', ['Office'])

        # Adding model 'Project'
        db.create_table('devcup_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('contractor', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('usercontributed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('budget', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('progress', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('like', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dislike', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('address', self.gf('gmapsfield.fields.GoogleMapsField')(default='{ coordinates: [14.6001, 120.9843], zoom: 10, size: [400, 200] }')),
        ))
        db.send_create_signal('devcup', ['Project'])

        # Adding M2M table for field offices on 'Project'
        db.create_table('devcup_project_offices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['devcup.project'], null=False)),
            ('office', models.ForeignKey(orm['devcup.office'], null=False))
        ))
        db.create_unique('devcup_project_offices', ['project_id', 'office_id'])

        # Adding model 'Comment'
        db.create_table('devcup_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devcup.Project'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('devcup', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Office'
        db.delete_table('devcup_office')

        # Deleting model 'Project'
        db.delete_table('devcup_project')

        # Removing M2M table for field offices on 'Project'
        db.delete_table('devcup_project_offices')

        # Deleting model 'Comment'
        db.delete_table('devcup_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'devcup.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devcup.Project']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'devcup.office': {
            'Meta': {'object_name': 'Office'},
            'address': ('gmapsfield.fields.GoogleMapsField', [], {'default': "'{ coordinates: [14.6001, 120.9843], zoom: 10, size: [400, 200] }'"}),
            'contact_no': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'head': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'devcup.project': {
            'Meta': {'object_name': 'Project'},
            'address': ('gmapsfield.fields.GoogleMapsField', [], {'default': "'{ coordinates: [14.6001, 120.9843], zoom: 10, size: [400, 200] }'"}),
            'budget': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'contractor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dislike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'offices': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devcup.Office']", 'null': 'True', 'blank': 'True'}),
            'progress': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'usercontributed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['devcup']