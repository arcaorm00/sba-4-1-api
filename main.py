from flask import Flask
from flask_restful import Api
from com_sba_api.ext.db import url, db
from com_sba_api.ext.routes import initialize_routes
from com_sba_api.user.user_api import UserApi, Users 
from com_sba_api.item.item_api import ItemApi, Items
from com_sba_api.board.article_api import ArticleApi, Articles
from com_sba_api.user import user 
# python 파일을 특정하지 않고 디렉토리 이름을 참조하면 __init__.py를 찾는다.
from flask_cors import CORS

print('====== 1 ======')
app = Flask(__name__)
CORS(app)
app.register_blueprint(user)

print(url)

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

initialize_routes(api)

with app.app_context():
    db.create_all()

@app.route('/api/test')
def test():
    return {'test': 'Success'}