# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Price', fields ['item', 'quantity']
        db.create_unique(u'checkout_price', ['item_id', 'quantity'])


    def backwards(self, orm):
        # Removing unique constraint on 'Price', fields ['item', 'quantity']
        db.delete_unique(u'checkout_price', ['item_id', 'quantity'])


    models = {
        u'checkout.item': {
            'Meta': {'object_name': 'Item'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'checkout.price': {
            'Meta': {'ordering': "('-quantity',)", 'unique_together': "(('item', 'quantity'),)", 'object_name': 'Price'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['checkout.Item']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['checkout']