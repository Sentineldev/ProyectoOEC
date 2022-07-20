from flask import jsonify
class User:
    def __init__(self,completeUser=None,NoEmailuser=None,WithEmailUser=None):
        if completeUser != None:
            self.username = completeUser['username']
            self.password = completeUser['password']
            self.email = completeUser['email']  
            self.user_id = completeUser['user_id']
        elif NoEmailuser != None:
            self.username = NoEmailuser['username']
            self.password = NoEmailuser['password']
            self.email = None  
            self.user_id = None
        elif WithEmailUser != None:
            self.username = WithEmailUser['username']
            self.password = WithEmailUser['password']
            self.email = WithEmailUser['email']
            self.user_id = None
        else:
            self.username = None
            self.password = None
            self.email = None  
            self.user_id = None
        self.__isValidated = None

    #Getters
    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email
    def getUserId(self):
        return self.user_id
    def getIsValidated(self):
        return self.__isValidated

    #setters
    def setUsername(self,username):
        self.username = username
    def setUsername(self,password):
        self.password = password
    def setEmail(self,email):
        self.email = email
    def setUserId(self,user_id):
        self.user_id = user_id
    def setIsValidated(self,isValidated):
        self.__isValidated = isValidated

    #convertToJson

    def ToDict(self):
        return {
            "username":self.getUsername(),
            "password":self.getPassword(),
            "email":self.getEmail(),
            "user_id":self.getUserId(),
            "isValidated":self.getIsValidated()
        }