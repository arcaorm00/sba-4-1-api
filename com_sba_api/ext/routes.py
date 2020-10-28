from com_sba_api.resources.item import ItemApi, Items
from com_sba_api.resources.user import UserApi, Users, Auth, Access
from com_sba_api.resources.article import ArticleApi, Articles
from com_sba_api.resources.home import Home
from com_sba_api.resources.cabbage import Cabbage

def initialize_routes(api):
    print('====== 2 ======')
    api.add_resource(Home, '/api')
    api.add_resource(ItemApi, '/api/item/<string:id>')
    api.add_resource(Items, '/api/items')
    api.add_resource(UserApi, '/api/user/<string:id>')
    api.add_resource(Users, '/api/users')
    api.add_resource(Auth, '/api/auth')
    api.add_resource(Access, '/api/access')
    api.add_resource(ArticleApi, '/api/article/<string:id>')
    api.add_resource(Articles, '/api/articles')
    api.add_resource(Articles, '/api/cabbage')