from flask import Flask
from flask_restful import Api
from com_sba_api.ext.db import url, db
from com_sba_api.ext.routes import initialize_routes
from com_sba_api.item.item_api import ItemApi, Items
from com_sba_api.board.article_api import ArticlsApi, Articles
from com_sba_api.user import user
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(user)

print('====== url ======')
print(url)

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

initialize_routes(api)

with app.app_context():
    db.create_all()

@app.route('/api/test')
def test():
    return {'test': 'Success'}