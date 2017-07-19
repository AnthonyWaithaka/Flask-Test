# server.py

import re

email_list = []
email_counter = 0

class bluServer(object):
    
    def __init__(self):
        pass
    
    def getEmail(self, userEmail):
        global email_list
        global email_counter
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', userEmail)

        if match == None:
            return False
        else:
            email_counter += 1
            email_list.insert((email_counter-1), userEmail)
            return userEmail

    def checkRepeat(self, userEmail):
        global email_list
        global email_counter
        if self.getEmail(userEmail) is False:
            return True
        else:
            checker = False
            for i in range(email_counter-1):
                if email_list[i] == userEmail:
                    checker = True
                    return checker
            return checker