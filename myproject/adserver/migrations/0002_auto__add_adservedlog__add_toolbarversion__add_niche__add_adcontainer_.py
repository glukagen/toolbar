# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AdServedLog'
        db.create_table('adserver_adservedlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adserver.VisitLog'])),
            ('container_url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('container_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adserver.AdContainer'])),
        ))
        db.send_create_signal('adserver', ['AdServedLog'])

        # Adding model 'ToolbarVersion'
        db.create_table('adserver_toolbarversion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('injection_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('adserver', ['ToolbarVersion'])

        # Adding model 'Niche'
        db.create_table('adserver_niche', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url_pattern', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('adserver', ['Niche'])

        # Adding model 'AdContainer'
        db.create_table('adserver_adcontainer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dimension', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('container_base_url', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('adserver', ['AdContainer'])

        # Adding model 'SearchEngineQueryLog'
        db.create_table('adserver_searchenginequerylog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search_engine', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adserver.Users'])),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adserver.VisitLog'])),
        ))
        db.send_create_signal('adserver', ['SearchEngineQueryLog'])

        # Adding model 'Users'
        db.create_table('adserver_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('install_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('browser_list', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('OS', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('IP', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('force_uninstall', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('toolbar_version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adserver.ToolbarVersion'])),
        ))
        db.send_create_signal('adserver', ['Users'])

        # Adding model 'Affiliate'
        db.create_table('adserver_affiliate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('affiliate_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adserver.Users'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('adserver', ['Affiliate'])

        # Adding model 'VisitLog'
        db.create_table('adserver_visitlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_url', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adserver.Users'])),
            ('browser', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('IP', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('adserver', ['VisitLog'])


    def backwards(self, orm):
        
        # Deleting model 'AdServedLog'
        db.delete_table('adserver_adservedlog')

        # Deleting model 'ToolbarVersion'
        db.delete_table('adserver_toolbarversion')

        # Deleting model 'Niche'
        db.delete_table('adserver_niche')

        # Deleting model 'AdContainer'
        db.delete_table('adserver_adcontainer')

        # Deleting model 'SearchEngineQueryLog'
        db.delete_table('adserver_searchenginequerylog')

        # Deleting model 'Users'
        db.delete_table('adserver_users')

        # Deleting model 'Affiliate'
        db.delete_table('adserver_affiliate')

        # Deleting model 'VisitLog'
        db.delete_table('adserver_visitlog')


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
        'adserver.niche': {
            'Meta': {'object_name': 'Niche'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url_pattern': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
