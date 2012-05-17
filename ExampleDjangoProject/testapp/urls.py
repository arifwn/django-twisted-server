
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^favicon.ico', 'frontend.views.favicon', name='favicon'),
    url(r'^$', 'testapp.views.index', name='index'),
)
