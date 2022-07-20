from flask import Blueprint,request,Response,json
from os import makedirs
import os.path
from Controllers.UserController import UserController
from Controllers.ArticleController import ArticleController
bp = Blueprint('article', __name__,url_prefix="/article")




@bp.route("/register_article",methods=["POST"])
def register_article():
    try:
        title = request.form['title']
        body = request.form['body']
        user_id = request.form['user_id']
        user = UserController().SelectUserById(user_id)
        path = f"../client/src/user_images/{user.getUsername()}"
        if( not os.path.exists(path)):
            makedirs(path)
        f = request.files['image']
        path +=f"/{f.filename}"
        f.save(f"../client/src/user_images/{user.getUsername()}/{f.filename}") 
        ArticleController().insertArticle(user_id,title, body, f.filename)
        return Response(response="Ok",status=200)
    except Exception as e:
        print(e)
        return Response(response="Something went wrong!",status=400)


@bp.route("/get_articles/",methods=['GET'])
def get_articles():
    try:
        data = ArticleController().getAllArticles()
        return Response(response=json.dumps(data),status=200)
    except:
       return Response(response="Something went wrong!",status=400) 

@bp.route("/delete_article/<article_id>",methods=['DELETE'])
def delete_article(article_id):
    try:
        ArticleController().DeleteArticle(article_id)
    except Exception as e:
        print(e)
        return Response(response="Something went wrong",status=400)
    return Response(response="test",status=200)