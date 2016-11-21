NginxTest
=========

This project provides some helpers to write functional tests against
an Nginx server.

Prerequisites
-----------
For running this test, please make you have following installed

- Python 2.7+
- pip
- unittest2
- webtest
- mekotemplate

The NginxServer class
---------------------

This project provides a class to drive an Nginx server. The
class has two main method to start and stop a local Nginx
server and takes care of the gory details.

When initialized, the class creates an Nginx configuration on
the fly given a few options, and runs an Nginx server in
a child process in a fresh directory.

Once the server is started, the stdout, stderr and access/errors
logs are intercepted by the class so they can be asserted in the
tests. The stop method kills the server.

Sample Nginx tests using WebTest::

    import unittest2
    from webtest import TestApp
    from nginxtest.server import NginxServer


    class TestNginx(unittest2.TestCase):

        def setUp(self):
            self.nginx = NginxServer()
            self.nginx.start()
            self.app = TestApp(self.nginx.root_url)

        def tearDown(self):
            self.nginx.stop()

        def testHello(self):
            resp = self.app.get('/')
            self.assertEqual(resp.status_int, 200)
            self.assertTrue('Welcome to nginx!' in resp.body)


How to Run
-----------
In order to run these tests, run following command

:code:`sudo python -m unittest2 TestNginx`

Output

    Stopping server...
    
    .2016/11/21 07:54:12 [error] 3742#3742: *2 open() "/usr/share/nginx/html/hello" failed (2: No such file or directory), client: 127.0.0.1, server: , request: "GET /hello HTTP/1.1", host: "localhost:1984"
    
    Stopping server...
    .2016/11/21 07:54:12 [error] 3744#3744: *8 limiting requests, excess: 6.760 by zone "one", client: 127.0.0.1, server: , request: "GET / HTTP/1.1", host: "localhost:1984"
    
    Stopping server...
    .
    ----------------------------------------------------------------------
    
    Ran 3 tests in 1.118s

    OK


Expansion Scope
-----------

This project is limited currently (covering only a few scenarios).

This can further be expanded, here are some of the ideas that I would like to impelment:

- AB testing (test traffic routing)
- Cache expiration testing


