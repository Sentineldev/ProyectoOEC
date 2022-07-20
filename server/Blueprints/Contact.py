from flask import Blueprint,request,Response
from utils import SendEmail

bp = Blueprint("contact", __name__,url_prefix="/contact")


@bp.route("/sendMail",methods=["POST"])
def sendMail():
    print("hola")
    print(request.get_data(request.get_json()))
    try:
        json_data = request.get_json()
        response = SendEmail(json_data['title'], json_data['body'])
        if(response == True):
            return Response(response="Ok",status=200,mimetype="application/json")
        return Response(respose="Email not sended",status=400,mimetype="application/json")
    except:
        return Response(response="Something went wrong!",status=400,mimetype="application/json")