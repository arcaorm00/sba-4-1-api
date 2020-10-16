from typing import List
from flask_restful import Resource, reqparse
from com_sba_api.user.user_dao import UserDao
from com_sba_api.user.user_dto import UserDto

class UserApi(Resource):

    def __init__(self):
        parser = reqparse.RequestParser() # only allow price changes, no name changes allowed
        self.dao = UserDao

    def get(self, name):
        item = self.dao.find_by_name(name)
        
        if item:
            return item.json()

        return {'message': 'Item not found'}, 404

class Users(Resource):
    def get(self):
        return {'user': list(map(lambda user: user.json(), UserDao.find_all()))}