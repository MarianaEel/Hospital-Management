import json
from flask_restful import reqparse
from numpy import empty
from module.user_management.management_api import management_api
from module.database_api.mongo_api import MongoAPI
from module.speech2text.stt import stt_api
from os.path import exists

"""
Managemetn_factory.py:
This file is a factory to produce API Resource class needed by Flask API.
Use "management_api" as prototype to produce API Resource class. Check "management_api.py" in 

Chats module currently use override to implement speech to text.
"""

class patients(management_api):
    def __init__(self,dir=None) -> None:
        self.name = "patients"
        self.mongo_obj = MongoAPI()

class staffs(management_api):
    def __init__(self,dir=None) -> None:
        self.name = "staffs"
        self.mongo_obj = MongoAPI()

class datas(management_api):
    def __init__(self,dir=None) -> None:
        self.name = "datas"
        self.mongo_obj = MongoAPI()

class chats(management_api):
    def __init__(self,dir=None) -> None:
        self.name = "chats"
        self.mongo_obj = MongoAPI()
    
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        for key in self.mongo_obj.data[self.name][0]["key"]:
            parser.add_argument(key, required=True)  # add args
        args = parser.parse_args()  # parse collections to dictionary
        
        # read our database
        data = self.mongo_obj.database[self.name].find_one(
            {"id": args['id']}, {"_id": 0})
        if data is None:
            #check if audio file exist
            if (exists(args["voice"])):
                stt_objects= stt_api()
                args["textdata"] = stt_objects.speech_to_text(args["voice"])
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
            #check if audio file exist
            if (exists(args["voice"])):
                stt_objects= stt_api()
                args["textdata"] = stt_objects.speech_to_text(args["voice"])
            # save back to database
            output = self.mongo_obj.update(self.name, filt, args)
            # return data and 200 OK
            return {'data': output}, 200

        else:
            # otherwise the id does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404

if __name__ == '__main__':
    """
    following comment is for testing
    """
    # print("testing")
    # productdir = "./data/fac_product.json"
    # with open(productdir) as json_file:
    #     product = json.load(json_file)
    # for pname in product:
    #     newproduct =  management_factory(Resource,pname)
    #     print("testing "+newproduct.name)
    #     print(newproduct.name)
    #     print(newproduct.product[newproduct.name][0]["csv"])
    pass