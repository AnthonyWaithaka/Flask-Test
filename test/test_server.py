# test_server.py

import unittest

from app.server import bluServer 


class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.bServer = bluServer()

    def test_email(self):
        self.assertEqual(self.bServer.getEmail('something@yes.com'), 'something@yes.com', "Not a Valid Email Address")
    
    def test_email_repetition(self):
        new_email = self.bServer.getEmail('something@yes.com')
        new_email_2 = self.bServer.getEmail("1122.13.com") #This is false, therefore, it should not be allowed to pass the first test and be used in the second one
        new_email_2 = self.bServer.getEmail("1122@13.com")
        self.assertEqual(self.bServer.checkRepeat('something@no.com'), False, "Email address already in use")