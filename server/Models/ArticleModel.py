from db import get_db,close_db
class ArticleModel:
    def __init__(self):
        pass


    def insertArticle(self,user_id,title,body,imgUrl):
        db,c= get_db()

        c.execute(
            """
            INSERT INTO articles(user_id,title,body,img_url)
            VALUES(%s,%s,%s,%s)
            """,(user_id,title,body,imgUrl)
        )
        db.commit()
        close_db()

    def getAllArticles(self):
        db,c = get_db()
        c.execute(
            """
            SELECT * FROM oec_users.articles
            JOIN users ON users.user_id = articles.user_id;
            """
        )
        data = c.fetchall()
        close_db()
        return data

    def DeleteArticle(self,article_id):
        db,c = get_db()

        c.execute(
            "DELETE FROM articles WHERE article_id = %s",(article_id,)
        )
        db.commit()
        close_db()