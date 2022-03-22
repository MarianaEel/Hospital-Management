from pymongo import MongoClient
import json
# from flask import Flask, request, json, Response

class MongoAPI:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:5000/")  
        infodir = "./data/mongo_info.json"
        with open(infodir) as json_file:
            mongoinfo = json.load(json_file)

        self.database = self.client[mongoinfo['database']]
        self.collections = mongoinfo['collection']
        self.data = mongoinfo

    def read(self,collection, data={}):
        documents = self.database[collection].find(data)
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, collection, data):
        response = self.database[collection].insert_one(data)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output
    
    def update(self, collection, filter, data):
        updated_data = {"$set": data}
        response = self.database[collection].update_one(filter, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, collection, mode, data):
        if mode == 0:
            response = self.database[collection].delete_one(data)
        elif mode == 1:
            response = self.database[collection].delete_many(data)
        else :
            return "mode 0 for delete one, mode 1 for delete many"
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

if __name__ == '__main__':
    mongo_obj = MongoAPI()
    print("checking database name")
    print(mongo_obj.client.list_database_names())

    print("testing collection")
    print(mongo_obj.database.list_collection_names())
    print("testing collection end")

    jason = {
        "id":"106",
        "name":"mason",
        "age":"12"    
    }
    filt = {
        "name":"mason"
    }
    update = {
        "age":"19"   
    }
    data=mongo_obj.database["patients"].find_one({"id":"104"},{"_id": 0})
    print(data)
    print(data is not None)


    # print("testing write")
    # mongo_obj.write("patients",jason)
    # print(json.dumps(mongo_obj.read("patients"), indent=4))
    # print(len(list(mongo_obj.database["patients"].find({"id":10086}))))


    # print("testing update")
    # mongo_obj.update("patients",filt,update)
    # print(json.dumps(mongo_obj.read("patients"), indent=4))


    # print("delete")
    # todelete = { "id": "106" }
    # print(json.dumps(mongo_obj.delete("patients", 1,todelete), indent=4))
    # print("after delete")
    # print(json.dumps(mongo_obj.read("patients"), indent=4))