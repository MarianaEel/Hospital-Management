from abc import ABCMeta, abstractstaticmethod
from flask_restful import Resource, reqparse
import pandas as pd
import json
from ..database_api import mongo_api


class management_api_interface(Resource):
    '''a interface for api class'''
    @abstractstaticmethod
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class management_api(management_api_interface):
    '''define a api prototype for extention'''

    def __init__(self, dir=None) -> None:
        self.name = "name"
        self.mongo_obj = mongo_api.MongoAPI()
        # productdir=dir if dir is not None else "./data/mongo_info.json"
        # with open(productdir) as json_file:
        #     self.product = json.load(json_file)

    def get(self):
        data = self.mongo_obj.read(self.name)  # read
        # data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        for key in self.mongo_obj.data[self.name][0]["key"]:
            parser.add_argument(key, required=True)  # add args
        args = parser.parse_args()  # parse collections to dictionary

        # read our database
        data = self.mongo_obj.database[self.name].find_one(
            {"id": args['id']}, {"_id": 0})
        if data is None:
            output = self.mongo_obj.write(self.name, args)
            return {'data': output}, 200  # return data with 200 OK
        else:
            return {
                'message': f"'{args['id']}' already exists."
            }, 401

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        for key in self.mongo_obj.data[self.name][0]["key"]:
            if key == "id":
                parser.add_argument(key, required=True)  # add args
            else:
                parser.add_argument(key, required=False)  # add args
        args = parser.parse_args()  # parse collections to dictionary

        filt = {"id": args['id']}
        # read our database
        data = self.mongo_obj.database[self.name].find_one({"id": args['id']})
        if data is not None:
            # save back to database
            output = self.mongo_obj.update(self.name, filt, args)
            # return data and 200 OK
            return {'data': output}, 200

        else:
            # otherwise the id does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404

    def delete(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add id arg
        args = parser.parse_args()  # parse collections to dictionary

        # read our database
        data = self.mongo_obj.database[self.name].find_one({"id": args['id']})
        if data is not None:
            # delete from db
            output = self.mongo_obj.delete(self.name, 0, {"id": args['id']})
            # return data and 200 OK
            return {'data': output}, 200
        else:
            # otherwise we return 404 because id does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404
