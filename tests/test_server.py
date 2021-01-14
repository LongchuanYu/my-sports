import unittest
from app import create_app

class CreateApp(unittest.TestCase):
    def tearDown(self):
        print('trearDown')

    def setUp(self):
        self.app = create_app().test_client()
    
    def test_connect_server(self):
        resp = self.app.get('/test')
        assert 'test123' in str(resp.data)