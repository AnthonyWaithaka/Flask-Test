# test_server.py

import unittest

from app.server import bluServer


class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.bServer = bluServer()

    def test_email_is_valid(self):
        self.assertNotEqual(self.bServer.validateEmail('something@yes.com'), False, "Not a Valid Email Address")

    def test_create_client_tAndC_fail(self):
        new_client = self.bServer.createClient('something@yes.com', 'aaa1111', True)
        self.assertNotEqual(new_client, 1, "Must Accept Terms and Conditions")

    def test_create_client_email_valid(self):
        new_client = self.bServer.createClient('something@yes.com', 'aaa1111', True)
        self.assertNotEqual(new_client, 2, "Invalid Email Address")

    def test_create_client_email_repetition(self):
        new_client = self.bServer.createClient('something@yes.com', 'aaa1111', True)
        new_client2 = self.bServer.createClient('something@no.com', 'bbb1122', True)
        self.assertNotEqual(new_client2, 3, "Client Email address already in use")

    def test_create_client_password_repetition(self):
        new_client = self.bServer.createClient('something@yes.com', 'aaa1122', True)
        new_client2 = self.bServer.createClient('something@yes.com', 'aaa1122', True)
        self.assertNotEqual(new_client2, 4, "Client Password already in use")