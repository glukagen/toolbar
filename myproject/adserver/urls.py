from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.adserver.views',
    (r'^$','index'),
    (r'^(?P<poll_id>\d+)/$','detail'),
    (r'^(?P<poll_id>\d+)/results/$','results'),
    (r'^(?P<poll_id>\d+)/vote/$','vote'),
    (r'^(?P<width>\d+)/(?P<height>\d+)/','container'),
    (r'dashboard/','dashboard'),
    (r'visitlog/','visit_request'),
    (r'container/','dashboard'),
    (r'showrequests','show_data'),
)


 