from typing import List
from flask import request, jsonify
from flask_restful import Resource, reqparse
from com_sba_api.user.user_dao import UserDao
from com_sba_api.user.user_dto import UserDto, UserVo
import json

parser = reqparse.RequestParser()
parser.add_argument('userid', type=str, required=True, help='This field should be a userid')
parser.add_argument('password', type=str, required=True, help='This field should be a password')

class UserApi(Resource):

    # def __init__(self):
    #     parser = reqparse.RequestParser() # only allow price changes, no name changes allowed
    #     self.dao = UserDao
    
    @staticmethod
    def post():
        args = parser.parse_args()
        print(f'User {args["id"]} added')
        params = json.loads(request.get_data(), encoding='utf-8')
        if len(params) == 0:
            return 'No parameter'

        params_str = ''
        for key in params.key():
            params_str += 'key: {}, value: {}\n'.format(key, params[key])
        return {'code': 0, 'message': 'SUCCESS'}, 200

    @staticmethod
    def get(id):
        print(f'User {id} added')

        try:
            user = UserDao.find_by_id(id)
            if user:
                return user.json()
        except Exception as e:
            return {'message': 'Item not found'}, 404
    
    @staticmethod
    def update():
        args = parser.parse_args()
        print(f'User {args["id"]} updated')
        return {'code': 0, 'message': 'SUCCESS'}
    
    @staticmethod
    def delete():
        args = parser.parse_args()
        print(f'User {args["id"]} deleted')
        return {'code': 0, 'message': 'SUCCESS'}, 200
    

class Users(Resource):

    def post(self):
        u_dao = UserDao()
        u_dao.insert_many('users')

    def get(self):
        return {'user': list(map(lambda user: user.json(), UserDao.find_all()))}

class Auth(Resource):
    def post(self):
        body = request.get_json()
        user = UserDto(**body)
        UserDao.save(user)
        id = user.userid
        return {'id': str(id)}, 200
    
class Access(Resource):
    def post(self):
        args = parser.parse_args()
        user = UserVo()
        user.userid = args.userid
        user.password = args.password
        print(user.userid)
        print(user.password)
        data = UserDao.login(user)
        return data[0], 200