from abc import ABCMeta, abstractstaticmethod
from flask_restful import Resource, reqparse
import pandas as pd
import json

class management_api_interface(Resource):
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
    def __init__(self,dir=None) -> None:
        self.name = "name"
        self.productdir=dir if dir is not None else "./data/fac_product.json"
        with open(self.productdir) as json_file:
            self.product = json.load(json_file)

    def get(self):
        data = pd.read_csv(self.product[self.name][0]["csv"])  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        for column in self.product[self.name][0]["argument"]:
            parser.add_argument(column, required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv(self.product[self.name][0]["csv"])

        if int(args['id']) in list(data['id']):
            return {
                'message': f"'{args['id']}' already exists."
            }, 401
        else:
            # create new dataframe containing new values
            new_data = pd.DataFrame()
            for column in self.product[self.name][0]["argument"]:
                new_data[column]=[args[column]]
            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            # save back to CSV
            data.to_csv(self.product[self.name][0]["csv"], index=False)
            return {'data': data.to_dict()}, 200  # return data with 200 OK

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        for column in self.product[self.name][0]["argument"]:
            if column =="id":
                parser.add_argument(column, required=True)  # add args
            else:
                parser.add_argument(column, required=False)  # add args
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv(self.product[self.name][0]["csv"])

        if int(args['id']) in list(data['id']):
            # # evaluate strings of lists to lists
            # data['locations'] = data['locations'].apply(
            #     lambda x: ast.literal_eval(x)
            # )

            # select our user
            user_data = data[data['id'] == int(args['id'])]

            for arg in args:
                user_data.loc[int(args['id']), arg] = args[arg]

            # save back to CSV
            data[data['id'] == int(args['id'])] = user_data
            data.to_csv(self.product[self.name][0]["csv"], index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise the id does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404


    def delete(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add id arg
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv(self.product[self.name][0]["csv"])
        
        if int(args['id']) in list(data['id']):
            # remove data entry matching given id
            data = data[data['id'] != int(args['id'])]
            
            # save back to CSV
            data.to_csv(self.product[self.name][0]["csv"], index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        else:
            # otherwise we return 404 because id does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404