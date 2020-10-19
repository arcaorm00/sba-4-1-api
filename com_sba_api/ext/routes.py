from com_sba_api.item.item_api import ItemApi
from com_sba_api.home.home_api import Home

def initialize_routes(api):
    api.add_resource(Home, '/api')
    api.add_resource(ItemApi, '/api/items')