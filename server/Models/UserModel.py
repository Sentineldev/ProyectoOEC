from werkzeug.security import generate_password_hash,check_password_hash
from db import get_db,close_db
from Classes.User import User

class UserModel:



    def SelectUserByUsername(self,username):
        db,c = get_db()
        c.execute(
            """
            SELECT * FROM users WHERE username = %s
            """,(username,)
        )
        username = c.fetchone()
        close_db()
        return username == None
    def InsertUser(self,user):
        db,c = get_db()

        c.execute(
            """
            INSERT INTO users(username,password,email)
            VALUES(%s,%s,%s)
            """,(
                user.getUsername(),
                generate_password_hash(user.getPassword()),
                user.getEmail()
            )
        )
        db.commit()
        close_db()
    def LoggedInUser(self,user):
        db,c = get_db()
        c.execute(
            """
            SELECT * FROM users WHERE username = %s
            """,(user.getUsername(),)
        )
        fetched_user = User(c.fetchone())
        close_db()
        if(check_password_hash(fetched_user.getPassword(), user.getPassword())):
            fetched_user.setIsValidated(True)
        else:
            fetched_user.setIsValidated(False)
        return fetched_user


    def SelectUserById(self,user_id):
        db,c = get_db()
        c.execute(
            """
            SELECT * FROM users WHERE user_id = %s
            """ ,(user_id,)
        )
        fetched_user = User(c.fetchone())
        
        close_db()
        return fetched_user