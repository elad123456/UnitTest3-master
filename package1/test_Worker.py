from unittest import TestCase
from package1.Worker import *
from unittest.mock import patch

class TestWorker(TestCase):
    def setUp(self):
        self.worker=Worker('elad','ratner',1999,5,2,'rotchild 5','israel')

    def test_location(self):
        with patch('package1.Worker.requests.get') as rg_mock:
            rg_mock.return_value.ok=True
            rg_mock.return_value.text='success'
            self.assertEqual(self.worker.location(),'success')
        with patch('package1.Worker.requests.get') as rg_mock:
            rg_mock.return_value.ok=False
            rg_mock.return_value.text='success'
            self.assertEqual(self.worker.location(),'Bad response!')

