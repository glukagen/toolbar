from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^tracking/', include('tracking.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^main/?$', 'clicks.views.index'),
    (r'^sentry/', include('sentry.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^reports/add-subids/?', 'clicks.views.register_sales'),
    (r'^reports/view-sales/?', 'clicks.views.view_sales'),
    (r'^redirect/(?P<visitor_id>[^/]+)/(?P<position>[^/]+)/?(?P<linktag>[^/]+)?','clicks.views.go_to_offer'),#outgoing click
    (r'^exit/(?P<visitor_id>[^/]+)','clicks.views.show_exit_page'),#exit page triggered
    (r'^exitclick/(?P<visitor_id>[^/]+)/(?P<position>[^/]+)/?(?P<linktag>[^/]+)?','clicks.views.go_to_offer_from_exit'),#outgoing click
    (r'^([^/]+)','clicks.views.show_main_page'),#incoming clicks...
    
)
