# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Review.nutrition_serving'
        db.add_column(u'reviews_review', 'nutrition_serving',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)


        # Changing field 'Review.nutrition'
        db.alter_column(u'reviews_review', 'nutrition', self.gf('django.db.models.fields.CharField')(max_length=250))

    def backwards(self, orm):
        # Deleting field 'Review.nutrition_serving'
        db.delete_column(u'reviews_review', 'nutrition_serving')


        # Changing field 'Review.nutrition'
        db.alter_column(u'reviews_review', 'nutrition', self.gf('django.db.models.fields.TextField')())

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
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        }
    }

    complete_apps = ['reviews']