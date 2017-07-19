# test_server.py

import unittest

from app.server import bluServer 


class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.bServer = bluServer()

    def test_email_is_valid(self):
        self.assertNotEqual(self.bServer.validateEmail('something@yes.com'), False, "Not a Valid Email Address")
    
    def test_email_repetition(self):
        new_email = self.bServer.validateEmail('something@yes.com')
        new_email_2 = self.bServer.validateEmail("1122.13.com") #This is false, therefore, it should not be allowed to pass the first test and be used in the second one
        new_email_3 = self.bServer.validateEmail("1122@13.com")
        self.assertEqual(self.bServer.checkEmailRepeat('something@yes.com'), False, "Email address already in use")

    def test_create_client_tAndC_fail(self):
        new_client = self.bServer.createClient('something@yes.com', 'aaa1123', True)
        self.assertEqual(new_client, 1, "Must Accept Terms and Conditions")
        self.assertEqual(new_client, 2, "User Email Invalid")

    def test_create_client_email_repetition(self):
        new_client = self.bServer.createClient('something@yes.com', 'aaa1123', True)
        new_client2 = self.bServer.createClient('something@yes.com', 'bbb1123', True)
        self.assertNotEqual(new_client2, 3, "Client Email address already in use")

    def test_create_client_password_repetition(self):
        new_client = self.bServer.createClient('something@yes.com', 'aaa1123', True)
        new_client2 = self.bServer.createClient('something@no.com', 'aaa1123', True)
        self.assertNotEqual(new_client2, 4, "Client Password already in use")