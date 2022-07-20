from Models.UserModel import UserModel


class UserController:
    def __init__(self):
        self.UserModel = UserModel()
        pass

    def SelectUserByUsername(self,username):
        return self.UserModel.SelectUserByUsername(username)        
    def InsertUser(self,user):
        self.UserModel.InsertUser(user)

    def LoggedInUser(self,user):
        return self.UserModel.LoggedInUser(user)

    def SelectUserById(self,user_id):
        return self.UserModel.SelectUserById(user_id)
    