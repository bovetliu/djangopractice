from django.test import TestCase
from simpletcp.tcpserver import TCPServer

# Create your tests here.
class RegularTest(TestCase):

    def test_001(self):
        self.assertTrue(1 == 1)

    def test_002(self):
        self.assertTrue(2 == 2)

    def test_003(self):
        self.assertTrue(3 == 3)

    def test_004(self):
        self.assertTrue(4 == 4)

