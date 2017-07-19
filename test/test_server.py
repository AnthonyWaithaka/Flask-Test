# test_server.py

import unittest

from app.server import bluServer
from app.server import bluClient


class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.bServer = bluServer()

    def test_email_is_valid(self):
        self.assertNotEqual(self.bServer.validateEmail('something@yes.com'), False, "Not a Valid Email Address")

    def test_create_client_tAndC_fail(self):
        new_client = self.bServer.createClient('something@yes.com', 'thisguy', 'aaa1111', True)
        self.assertNotEqual(new_client, 1, "Must Accept Terms and Conditions")

    def test_create_client_email_valid(self):
        new_client = self.bServer.createClient('something@yes.com', 'thisguy', 'aaa1111', True)
        self.assertNotEqual(new_client, 2, "Invalid Email Address")

    def test_create_client_email_repetition(self):
        new_client = self.bServer.createClient('something@yes.com', 'thisguy', 'aaa1111', True)
        new_client2 = self.bServer.createClient('something@no.com', 'thatguy', 'bbb1112', True)
        self.assertNotEqual(new_client2, 3, "Client Email address already in use")

    def test_create_client_password_repetition(self):
        new_client = self.bServer.createClient('something1@yes.com', 'whichguy', 'aaa1113', True)
        new_client2 = self.bServer.createClient('something1@no.com', 'anotherguy', 'aaa1114', True)
        self.assertNotEqual(new_client2, 4, "Client Password already in use")

    def test_create_client_username_repetition(self):
        new_client = self.bServer.createClient('something2@yes.com', 'thisone', 'aaa1115', True)
        new_client2 = self.bServer.createClient('something2@no.com', 'thatone', 'aaa1116', True)
        self.assertNotEqual(new_client2, 4, "Client Username already in use")

    def test_client_is_valid_object(self):
        new_client = self.bServer.createClient('something@yes.com', 'theseguys', 'aaa1117', True)
        new_client2 = self.bServer.createClient('something3@yes.com', 'thoseguys', 'aaa1118', True)
        self.assertIsInstance(new_client2, bluClient, "Invalid Client Object")
    #Observation, cannot use the same data pairs as previous test function. It will raise an error