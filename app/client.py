from app.bucketlist import bluBucketList

class bluClient(object):
    def __init__(self, userId, userEmail, userPassword):
        self.userId = userId
        self.userEmail = userEmail
        self.userPassword = userPassword

    def viewList(self):
        newBucketList = bluBucketList()
        return newBucketList
