import logging
from flask import Blueprint
from flask_restful import Api
from com_sba_api.user.user_api import UserApi

user = Blueprint('user', __name__, url_prefix='/api/user')
users = Blueprint('users', __name__, url_prefix='/api/users')
auth = Blueprint('auth', __name__, url_prefix='/api/auth')
access = Blueprint('access', __name__, url_prefix='/api/access')
article = Blueprint('article', __name__, url_prefix='/api/article')
articles = Blueprint('articles', __name__, url_prefix='/api/articles')
cabbage = Blueprint('cabbage', __name__, url_prefix='/api/cabbage')

api = Api(user)
api = Api(users)
api = Api(auth)
print('====== 3 ======')
api = Api(access)
print('====== 4 ======')
api = Api(article)
api = Api(articles)
api = Api(cabbage)

@user.errorhandler(500)
def user_server_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occured.', 500

@home.errorhandler(500)
def home_server_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occured.', 500

@article.errorhandler(500)
def article_server_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occured.', 500

@cabbage.errorhandler(500)
def cabbage_server_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occured.', 500