from typing import List
from flask_restful import Resource, reqparse
from com_sba_api.item.item_dao import ItemDao
from com_sba_api.item.item_dto import ItemDto

class ItemApi(Resource):

    def __init__(self):
        parser = reqparse.RequestParser() # only allow price changes, no name changes allowed
        self.dao = ItemDao

    def get(self, name):
        item = self.dao.find_by_name(name)
        
        if item:
            return item.json()

        return {'message': 'Item not found'}, 404