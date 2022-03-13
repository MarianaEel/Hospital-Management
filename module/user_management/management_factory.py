import json
from module.user_management.management_api import management_api


class patients(management_api):
    def __init__(self,dir=None) -> None:
        self.name = "patients"
        self.productdir=dir if dir is not None else "./data/fac_product.json"
        with open(self.productdir) as json_file:
            self.product = json.load(json_file)

class staffs(management_api):
    def __init__(self,dir=None) -> None:
        self.name = "staffs"
        self.productdir=dir if dir is not None else "./data/fac_product.json"
        with open(self.productdir) as json_file:
            self.product = json.load(json_file)

class datas(management_api):
    def __init__(self,dir=None) -> None:
        self.name = "datas"
        self.productdir=dir if dir is not None else "./data/fac_product.json"
        with open(self.productdir) as json_file:
            self.product = json.load(json_file)

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