'''
HPD Data Feeds API
'''

import requests

class HPD:
    def __init__(self,ID,Key):
        '''
        (Create HPD Object)
        (Ex) Object = HPD.HPD('API ID' , 'API Key')
        '''
        self.id = ID
        self.key = Key


    def validation(self,statusCode):
        '''
        Validates whether the search was successful or not.

        '''
        if statusCode == 403:
            print 'Error Code:403 \n Make sure your APP ID/APP Key are correct'
            print 'APP ID: ', self.id,'  App Key: ',self.key
    
        elif statusCode == 0:
            print 'Error Code:0 \n Make sure your firewall isn\'t blocking any connections'
        
        elif statusCode == 200:
            return True
        
    def setID(self, newID):
        '''
        (Set a new ID for an object)

        (Example)

        object.setID(12345)
            ==> Assigns a new ID number(12345) to the object
        '''
        self.id = newID

    def setKey(self,newKey):
        '''
        (Set a new key for an object)

        (Example)

        object.setKey(56789)
            ==> Assigns a new key number(56789) to the object
        '''
        self.key = str(newKey)
        
    def getID(self):
        '''
        (Check to make sure the ID entered for an object was correct)

        (Example)

        object.getID()
            ==> Returns the ID number for object
        '''
        print self.id
        return self.id
    
    def getKey(self):
        '''
        (Check to make sure the Key entered for an object was correct)

        (Example)

        object.getKey()
            ==> Returns the key for object
        '''
        print self.key
        return self.key

    def getHPDFeed(self):
        '''
        (Search Press releases related to HPD)
        (Example)
        
        Object.getHPDFeed()
                ==> Searches for Press Releases related to HPD
             
        '''
        self.r = requests.get("https://api.cityofnewyork.us/hpd/v1/data-feeds/"+
                              "pr_rss.xml" +
                              "?app_id=" + self.id +
                              "&app_key=" +self.key)
        self.sCode = self.r.status_code
        print self.sCode
        self.validator = self.validation(self.sCode)
        if  self.validator == True:
            return self.r
