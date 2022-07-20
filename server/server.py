from flask import Flask,jsonify,request
import db
from db import get_db
from Blueprints import User,Article,Contact
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY="123123",
        FLASK_DATABASE_HOST="localhost",
        FLASK_DATABASE_USER="root",
        FLASK_DATABASE_PASSWORD="70242526",
        FLASK_DATABASE="oec_users"
    )
    db.init_app(app)    
    app.register_blueprint(User.bp)
    app.register_blueprint(Article.bp)
    app.register_blueprint(Contact.bp)

    @app.route("/")
    def index():
        db,c = get_db()
        c.execute("SELECT * FROM users")
        result = c.fetchall()
        return jsonify(result)

    @app.route("/test",methods=['POST','GET'])
    def test():
        try:
            print("hola")
            print(request.get_json())
            return jsonify({"members":['Member_1','Member_2','Member_3']})
        except Exception as e:
            print(e)
            return "hola"
    return app


app = create_app()