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

- Output


Expansion Scope
-----------

This project is limited currently (covering only a few scenarios).

This can further be expanded, here are some of the ideas that I would like to impelment:

- AB testing (test traffic routing)
- Cache expiration testing


