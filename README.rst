=====================
Django Twisted Server
=====================

A Django WSGI Server

Requirement
===========
Twisted version 10 or later.

Usage
=====

As Development Server
---------------------

First, copy ``servicemaker.py`` and ``twisted`` folder to your project directory.
Edit ``servicemaker.py`` and replace following line::
    
    # Replace this line with your wsgi script
    from ExampleDjangoProject import wsgi as django_wsgi


In your ``settings.py``:

* Make sure ``DEBUG = True``
* If you want to enable SSL::

    TWISTED_ENABLE_SSL = True
    TWISTED_SSL_CERT = './cert/cert.pem' # path to your certificate file
    TWISTED_SSL_KEY = './cert/key.pem' # path to your certificate key

* If you encounter problem with static files handling, edit your main ``urls.py`` as following::

    from django.conf.urls.defaults import patterns, include, url
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static
    from django.conf import settings
    
    
    urlpatterns = patterns('',
        # your urlconfigs...    
    )
    
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

To run the server, use ``twistd -n rundjserver``. If you omit ``-n``,
Twisted will run as daemon with pid saved in ``twistd.pid`` file.
To kill the daemon, use ``kill <pid>``.

You can access http server in http://127.0.0.1:8000 and https server in
https://127.0.0.1:8001.

As Production Server
---------------------

First, copy ``servicemaker.py`` and ``twisted`` folder to your project directory.
Edit ``servicemaker.py`` and replace following line::
    
    # Replace this line with your wsgi script
    from ExampleDjangoProject import wsgi as django_wsgi


In your ``settings.py``:

* Make sure ``DEBUG = False``
* Add following code::

    TWISTED_HTTP_PORT = 80 # for http request
    TWISTED_HTTPS_PORT = 443 # for https request
    TWISTED_LISTEN_ADDR = 'your.ip.address' # set to empty string to listen on all interface
    TWISTED_SERVE_STATIC = True # serve static contents too
    
    TWISTED_ENABLE_SSL = True
    TWISTED_SSL_CERT = '/path/to/cert/cert.pem' # use absolute path!
    TWISTED_SSL_KEY = '/path/to/cert/key.pem' # use absolute path!

To run the server, use ``twistd rundjserver``. You must run it as privileged user
since Twisted will listen on privileged ports.
Twisted will run as daemon with pid saved in ``twistd.pid`` file.
To kill the daemon, use ``kill <pid>``.
