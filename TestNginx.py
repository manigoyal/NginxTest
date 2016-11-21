import unittest2
from webtest import TestApp
from nginxtest.server import NginxServer


class TestNginx(unittest2.TestCase):

    def setUp(self):
	#Create NGINXServer class instance to control server start and stop
        self.nginx = NginxServer(**{'http_options':'limit_req_zone  $binary_remote_addr  zone=one:10m   rate=10r/s;',
				  'server_options':'limit_req zone=one burst=6 nodelay;'})
        self.nginx.start()
        self.app = TestApp(self.nginx.root_url)

    def tearDown(self):
        self.nginx.stop()
	print("Stopping server...")

    #Test HTTP Status code 200 
    def testCheckResponse200(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_int, 200)
        self.assertTrue('Welcome to nginx!' in resp.body)
	self.assertEqual(resp.content_type, 'text/html')

    #Test HTTP Status code 404 (hello location doesnt exist)
    def testCheckResponse404(self):
        resp = self.app.get('/hello', status=404)
        self.assertEqual(resp.status_int, 404)

    #Test HTTP Status code 503 (Due to rate limit)
    def testCheckResponse503(self):
        resp = self.app.get('/', status=200)
        resp = self.app.get('/', status=200)
        resp = self.app.get('/', status=200)
        resp = self.app.get('/', status=200)
        resp = self.app.get('/', status=200)
        resp = self.app.get('/', status=200)  
        resp = self.app.get('/', status=503)
        self.assertEqual(resp.status_int, 503)
       




      



          


        



