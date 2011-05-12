# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'request_data'
        db.create_table('adserver_request_data', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('val1', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('val2', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('adserver', ['request_data'])


    def backwards(self, orm):
        
        # Deleting model 'request_data'
        db.delete_table('adserver_request_data')


    models = {
        'adserver.adcontainer': {
            'Meta': {'object_name': 'AdContainer'},
            'container_base_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dimension': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'adserver.adservedlog': {
            'Meta': {'object_name': 'AdServedLog'},
            'container_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adserver.AdContainer']"}),
            'container_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'visit_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adserver.VisitLog']"})
        },
        'adserver.affiliate': {
            'Meta': {'object_name': 'Affiliate'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'affiliate_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adserver.Users']"})
        },
        'adserver.dummy_data': {
            'Meta': {'object_name': 'dummy_data'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'val1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'val2': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'val3': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'val4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'val5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'val6': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'val7': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'adserver.niche': {
            'Meta': {'object_name': 'Niche'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url_pattern': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'adserver.request_data': {
            'Meta': {'object_name': 'request_data'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'val1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'val2': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'adserver.searchenginequerylog': {
            'Meta': {'object_name': 'SearchEngineQueryLog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'search_engine': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adserver.Users']"}),
            'visit_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adserver.VisitLog']"})
        },
        'adserver.toolbarversion': {
            'Meta': {'object_name': 'ToolbarVersion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injection_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'adserver.users': {
            'IP': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Users'},
            'OS': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'browser_list': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'force_uninstall': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install_date': ('django.db.models.fields.DateTimeField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'toolbar_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adserver.ToolbarVersion']"}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'adserver.visitlog': {
            'IP': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'VisitLog'},
            'browser': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_url': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adserver.Users']"})
        }
    }

    complete_apps = ['adserver']
