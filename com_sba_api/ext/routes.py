from com_sba_api.item.item_api import ItemApi, Items
from com_sba_api.user.user_api import UserApi, Users, Auth, Access
from com_sba_api.board.article_api import ArticleApi, Articles
from com_sba_api.home.home_api import Home

def initialize_routes(api):
    api.add_resource(Home, '/api')
    api.add_resource(ItemApi, '/api/item/<string:id>')
    api.add_resource(Items, '/api/items')
    api.add_resource(UserApi, '/api/user/<string:id>')
    api.add_resource(Users, '/api/users')
    api.add_resource(Auth, '/api/auth')
    api.add_resource(Access, '/api/access')
    api.add_resource(ArticleApi, '/api/article/<string:id>')
    api.add_resource(Articles, '/api/articles')