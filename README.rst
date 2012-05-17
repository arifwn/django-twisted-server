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

First, copy `servicemaker.py` and `twisted` folder to your project directory.

In your `settings.py`:
* Make sure `DEBUG = TRUE`
* If you want to enable SSL:

    TWISTED_ENABLE_SSL = True
    TWISTED_SSL_CERT = './cert/cert.pem' # path to your certificate file
    TWISTED_SSL_KEY = './cert/key.pem' # path to your certificate key

To run the server, use `twistd -n rundjserver`. If you omit `-n`,
Twisted will run as daemon with pid saved in `twistd.pid` file.
To kill the daemon, use `kill <pid>`.

You can access http server in http://127.0.0.1:8000 and https server in
https://127.0.0.1:8001.

As Production Server
---------------------

First, copy `servicemaker.py` and `twisted` folder to your project directory.

In your `settings.py`:
* Make sure `DEBUG = False`
* Add following code:

    TWISTED_HTTP_PORT = 80 # for http request
    TWISTED_HTTPS_PORT = 443 # for https request
    TWISTED_LISTEN_ADDR = 'your.ip.address' # set to empty string to listen on all interface
    TWISTED_SERVE_STATIC = True # serve static contents too
    
    TWISTED_ENABLE_SSL = True
    TWISTED_SSL_CERT = '/path/to/cert/cert.pem' # use absolute path!
    TWISTED_SSL_KEY = '/path/to/cert/key.pem' # use absolute path!

To run the server, use `twistd rundjserver`. You must run it as privileged user
since Twisted will listen on privileged ports.
Twisted will run as daemon with pid saved in `twistd.pid` file.
To kill the daemon, use `kill <pid>`.
