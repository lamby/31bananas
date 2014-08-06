# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Review.published'
        db.delete_column(u'reviews_review', 'published')


    def backwards(self, orm):
        # Adding field 'Review.published'
        db.add_column(u'reviews_review', 'published',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        u'reviews.image': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('review', 'order'),)", 'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['reviews.Review']"})
        },
        u'reviews.review': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Review'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'date': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nutrition': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'nutrition_serving': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'score_banana': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'score_overall': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': 10}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        }
    }

    complete_apps = ['reviews']