from flask_restful import Resource, reqparse
from com_sba_api.board.article_dao import ArticleDao
from com_sba_api.board.article_dto import ArticleDto

class ArticleApi(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('userid', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('title', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('content', type=str, required=False, help='This field cannot be left blank')

    def post(self):
        data = self.parser.parse_args()
        article = ArticleDto(data['title'], data['content'], data['userid'], data['item_id'])
        try:
            article.save()
        except:
            return {'message': 'An error occured inserting the articls'}, 500
        
        return article.json(), 201

    def get(self, id):
        article = ArticleDao.find_by_id(id)
        if article:
            return article.json()

        return {'message': 'Article not found'}, 404

    def put(self, id):
        data = self.parser.parse_args()
        article = ArticleDao.find_by_id(id)

        article.title = data['title']
        article.content = data['content']
        article.save()
        return article.json()

class Articles(Resource):

    def get(self):
        return {'articles': list(map(lambda article: article.json(), ArticleDao.find_all()))}