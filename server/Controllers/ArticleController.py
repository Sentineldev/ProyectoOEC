from Models.ArticleModel import ArticleModel

class ArticleController:
    def __init__(self):
        self.ArticleModel = ArticleModel()

    def insertArticle(self,user_id,title,body,imgUrl):
        self.ArticleModel.insertArticle(user_id,title,body,imgUrl)

    def getAllArticles(self):
        return self.ArticleModel.getAllArticles()

    def DeleteArticle(self,article_id):
        self.ArticleModel.DeleteArticle(article_id)