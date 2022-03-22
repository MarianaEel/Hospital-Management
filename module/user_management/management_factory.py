import json
from module.user_management.management_api import management_api
from module.database_api.mongo_api import MongoAPI

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

# class management_factory():
#     @staticmethod
#     def generate_method(apitype):
#         if apitype=="patients":
#             return patients()
#         if apitype=="staffs":
#             return staffs()



if __name__ == '__main__':
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