
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect


def favicon(request):
    return redirect(settings.STATIC_URL + 'frontend/img/favicon.ico')

def index(request):
    t = get_template('testapp/index.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)
