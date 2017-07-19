# server.py

import re
from app.client import bluClient

client_email_list = []
client_password_list = []
client_id_list = []
client_list = {}
client_access_list = {}

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

    def checkUsernameRepeat(self, userName):
        global client_id_list

        checker = False
        for i in client_id_list:
            if i == userName:
                checker = True
                return checker
        return checker

    def createClient(self, userEmail, userName, userPassword, terms_and_conditions):
        global client_list
        global client_email_counter
        global client_email_list
        global client_id_list
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

        if self.checkUsernameRepeat(userName) is True:
            return 5

        client_email_list.append(userEmail)

        client_password_list.append(userPassword)
        
        client_id_list.append(userName)

        client_list.update({userName:(userEmail,userPassword)})

        #create a client object initialized with client_id, email_address and pwd
        newClient = bluClient(userName, userEmail, userPassword)

        #add client_id and associated object to client_access_list
        client_access_list.update({userName:newClient})

        #return the new client object
        return newClient

    def deleteClient(self, bluclient):
        #check if respective client_id exists as a key in client_access_list
        #if so, 
        # find userEmail and userPassword from client_list
        # delete userName, userEmail and userPassword from client_id_list client_email_list and client_password_list
        # delete key-pair for client_access_list and client_list
        #Tests: 
        # 1. object of type bluClient not passed as argument
        # 2. respective client_id does not exist in client_access_list
        # 3. client_id and object pair still exist in client_access_list or client_list
        # 4. client_id
        pass

    def viewClient(self, bluclient):
        #check if bluclient exists as a key in client_access_list
        #if so, 
        # return bluClient's bucketlist object
        #Tests:
        # 1. object of type bluClient not passed as argument
        # 2. client_id does not exist
        # 3. client_id does not exist in client_access_list
        # 4. function does not return bluBucketList object
        pass
    
    def searchClient(self, userName):
        #check if userName exists in client_id_list
        #if so, return userName
        #Tests:
        # 1. userName does not exist in client_id_list
        # 2. does not return userName
        pass
