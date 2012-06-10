=====================
Django Twisted Server
=====================

A Django WSGI Server.

Features
========

* Multithreaded server capable of serving concurrent request.
* SSL support out of the box.
* Optional Twisted features (epoll reactor, etc...)

Requirement
===========
Twisted version 10 or later.

Usage
=====

As Development Server
---------------------

First, copy ``twisted_wsgi`` and ``twisted`` folder to your project directory.
Edit ``servicemaker.py`` in ``twisted_wsgi`` folder and replace following line::
    
    # Replace this line with your settings module
    os.environ['DJANGO_SETTINGS_MODULE'] = 'ExampleDjangoProject.settings'


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

First, copy ``twisted_wsgi`` and ``twisted`` folder to your project directory.
Edit ``servicemaker.py`` in ``twisted_wsgi`` folder and replace following line::
    
    # Replace this line with your settings module
    os.environ['DJANGO_SETTINGS_MODULE'] = 'ExampleDjangoProject.settings'


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

For security, you should specify uid and gid under which the Twisted server will run. Otherwise,
the server will run under root user, obviously not good for security.

For example, to run the server under uid 1000 and gid 100 with above settings (http on port 80 and 
https on port 443), execute this command under root: ``twistd -u 1000 -g 100 rundjserver``. 
Twisted will first run as root to bind to selected ports, then shedding the privilege and
run as specified user (uid: 1000 and gid: 100).

TIPS: Use ``id <user>`` command to find uid and gid of a particular user.


Available Settings
==================

The following settings apply when you set ``DEBUG = True``. They are meant to be used for 
development server (i.e. runserver replacement). There is no autoreload feature yet, so
you will need to restart the server manually if you changed any of your code.

* ``TWISTED_DEBUG_LISTEN_ADDR = '127.0.0.1'`` listened address. Set to empty string ``''`` to 
  make Twisted listen on all available address.
* ``TWISTED_DEBUG_HTTP_PORT = '8000'`` port used to listen for incoming http request.
* ``TWISTED_DEBUG_HTTPS_PORT = '8001'`` port used to listen for incoming https request.


The following settings apply when you set ``DEBUG = False``. They are meant to be used for 
production server.

* ``TWISTED_SERVE_STATIC = True`` serve static media (``MEDIA_URL`` and ``STATIC_URL``) 
  using Twisted's static file handler.
* ``TWISTED_LISTEN_ADDR = ''`` listened address. Set to empty string ``''`` to 
  make Twisted listen on all available address.
* ``TWISTED_HTTP_PORT = '80'`` port used to listen for incoming http request.
* ``TWISTED_HTTPS_PORT = '443'`` port used to listen for incoming https request.

The following settings apply regardless of ``DEBUG`` value.

* ``TWISTED_ENABLE_SSL = False`` start https server in addition to http server.
* ``TWISTED_REDIRECT_TO_HTTPS = False`` redirect all incoming http request to https.
* ``TWISTED_SSL_CERT = './cert/cert.pem'`` ssl certificate used to serve https request.
  Although the default value uses relative path, you should use absolute path especially
  in production environment.
* ``TWISTED_SSL_KEY = './cert/key.pem'``` ssl certificate's key used to serve https request.
* ``TWISTED_THREADPOOL_MIN_SIZE = 2`` minimum number of threads available in the reactor's
  thread pool.
* ``TWISTED_THREADPOOL_MAX_SIZE = 10`` maximum number of threads in the reactor's thread pool.
