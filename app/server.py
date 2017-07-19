# server.py

import re
from app.client import bluClient

client_email_list = []
client_email_counter = 0
client_password_list = []
client_password_counter = 0
client_id_list = []
client_list = {}

class bluServer(object):
    
    def __init__(self):
        pass
    
    def validateEmail(self, userEmail):
        global client_email_list
        global client_email_counter
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', userEmail)

        if match == None:
            return False
        else:
            return userEmail

    def checkEmailRepeat(self, userEmail):
        global client_email_list
        global client_email_counter
        
        checker = False
        for i in client_email_list:
            if i == userEmail:
                checker = True
                return checker
        return checker
    
    def checkPasswordRepeat(self, userPassword):
        global client_password_list

        checker = False
        for i in client_password_list:
            if i == userPassword:
                checker = True
                return checker
        return checker

    def createClient(self, userEmail, userPassword, terms_and_conditions):
        global client_list
        global client_email_counter
        global client_email_list
        global client_password_counter
        global client_password_list

        if terms_and_conditions is False:
            return 1
        
        new_user_email = self.validateEmail(userEmail)
        
        if new_user_email is False:
            return 2

        if self.checkEmailRepeat(new_user_email) is True:
            return 3

        if self.checkPasswordRepeat(userPassword) is True:
            return 4

        client_email_counter += 1
        client_email_list.insert((client_email_counter-1), userEmail)

        client_password_counter += 1
        client_password_list.insert((client_password_counter-1), userPassword)
        
        #use client_email_counter as client_id
        client_id_list.append(client_email_counter)

        #add to client_list dictionary with {client_id:(client_email, pwd)}
        client_list.update({client_id_list[client_email_counter-1]:(client_email_list[client_email_counter-1],client_password_list[client_password_counter-1])})

        #create a client object initialized with client_id, email_address and pwd
        newClient = bluClient(client_id_list[client_email_counter-1], userEmail, userPassword)

        #return the new client object
        return newClient