from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^toolbar/', include('toolbar.foo.urls')),
    
    #(r'^$','index'),
    (r'^polls/',include('myproject.adserver.urls')),
    (r'^brcomm/',include('myproject.adserver.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # (r'^container/728', 'adserver.views.serve_container'),
    
)


#THIS TAKES UP SPACE