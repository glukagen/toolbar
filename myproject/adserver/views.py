# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from myproject.adserver.models import ToolbarVersion, Users, VisitLog, dummy_data
from django.core import serializers
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt


def serve_container(width=728,height=90,url=None):
    #This function will return a container of a certain size using params: url, dimension
    
    if width == 728 and height == 90:
        #Serve the webpage container called xxxxxxx
        pass
    
def index(request):
    pass

def container(request,width=0,height=0, *args):
    attr = {'width': width, 'height':height}
    message = "%s by %s" % (width, height)
    return render_to_response('polltemplates/container.html', {'message':message, 'attr':attr})
    #Ideally we would also load the actual html code which would be loaded inside the div tag of the above file
    #Container looks up width, height, userid, siteid, country, domainid, nicheid, etc and "finds" an ad container to plug into itself
    
def dashboard(request):
    return render_to_response('stats/dashboard.html', {})
    
def hi(request):
    return HttpResponse('HI')

def brcom_user_details(request):
    #This function recieves the user details on: ip, browser, OS, site_url
    #It does these in this order:
    #Update user's activity today
    #Update user's page visit today
    #Update user's ip, browser, OS if different
    #Update clicks to siteDomain today and page today
    #Get user's clientID and siteID
    #Modify all the url params for ad container
    #Return the jquery code
    pass


@csrf_exempt
def visit_request(request):
    r = dummy_data()
    r.val1 = request.method
    val2 = request.REQUEST
    r.val2 = str(val2)[:99]
    if request.method == 'POST':
        r.val3 = request.REQUEST.get('ip','no ip')
        r.val4 = request.REQUEST.get('toolbarid', 'no toolbar id')
        r.val5 = request.REQUEST.get('site', 'no site')
        r.val5 = request.REQUEST.get('site', 'no site')
        r.val7 = request.REQUEST.get('browser', 'no browser')
    r.save()
    #q = dummy_data().objects.all()
    #return HttpResponse('dgfdfg')
    #json_serializer = serializers.get_serializer("json")()
    return HttpResponse(simplejson.dumps({'result':'success'}))
    #return HttpResponse('success')


def show_data(request):
    list_data = '<br /> '.join([d.val1+' --- '+d.val2+ ' >>>>>>>>>>> '+ d.val3 + ', '+ d.val4 + ', '
                                + d.val5 + ', '+ d.val6 + ', '+ d.val7 + ', ' for d in dummy_data.objects.all()])
    return HttpResponse(list_data)
   