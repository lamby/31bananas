# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'reviews_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['reviews.Review'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('image_hash', self.gf('django.db.models.fields.CharField')(default='', max_length=8, blank=True)),
        ))
        db.send_create_signal(u'reviews', ['Image'])

        # Adding unique constraint on 'Image', fields ['review', 'order']
        db.create_unique(u'reviews_image', ['review_id', 'order'])


    def backwards(self, orm):
        # Removing unique constraint on 'Image', fields ['review', 'order']
        db.delete_unique(u'reviews_image', ['review_id', 'order'])

        # Deleting model 'Image'
        db.delete_table(u'reviews_image')


    models = {
        u'reviews.image': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('review', 'order'),)", 'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['reviews.Review']"})
        },
        u'reviews.review': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Review'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'date': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nutrition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        }
    }

    complete_apps = ['reviews']