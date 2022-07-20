from flask import Blueprint,request,jsonify,Response,json
from pprint import pprint
from Classes.User import User
from Controllers.UserController import UserController
bp = Blueprint('user',__name__,url_prefix="/user")

@bp.route("/register",methods=['POST'])
def register():
    try:
        user = User(WithEmailUser=request.get_json())
        Controller = UserController()
        if (not Controller.SelectUserByUsername(user.getUsername())):
            return Response(response="The user already exists!",status=409,mimetype="application/json")
        else:
            Controller.InsertUser(user)
    except Exception as e:
        print(e)
        return Response(response="Error, please check you are sending correct data!",status=400,mimetype="application/json")
    return Response(response="Successfully register!",status=200,mimetype="application/json")


@bp.route("/login",methods=['POST','GET'])
def login():
    print(request.get_json())
    try:
        Controller = UserController()
        user = User(NoEmailuser=request.get_json())
        user = Controller.LoggedInUser(user)
        if user.getIsValidated():
            return Response(response=json.dumps(user.ToDict()),status=200,mimetype="application/json")
        else:
            return Response(response="User not found",status=404,mimetype="application/json")
    except Exception as e:
        print(e)
        return Response(response="Something went wrong!",status=404,mimetype="application/json")
    return "Hello world!"