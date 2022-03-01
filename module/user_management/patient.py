import imp
from flask_restful import Resource, reqparse
import pandas as pd
import ast


class patients(Resource):
    def get(self):
        data = pd.read_csv('./data/patients.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('gender', required=True)
        parser.add_argument('age', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('./data/patients.csv')
        

        if int(args['id']) in list(data['id']):
            return {
                'message': f"'{args['id']}' already exists."
            }, 401
        else:
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'id': [args['id']],
                'name': [args['name']],
                'gender': [args['gender']],
                'age': [args['age']]
            })
            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            # save back to CSV
            data.to_csv('./data/patients.csv', index=False)
            return {'data': data.to_dict()}, 200  # return data with 200 OK
            
    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add args
        parser.add_argument('name', required=False)
        parser.add_argument('gender', required=False)
        parser.add_argument('age', required=False)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('./data/patients.csv')
        
        print(data)

        if int(args['id']) in list(data['id']):
            # # evaluate strings of lists to lists
            # data['locations'] = data['locations'].apply(
            #     lambda x: ast.literal_eval(x)
            # )

            print("in id")

            # select our user
            user_data = data[data['id'] == int(args['id'])]

            print(user_data)

            # update user's name if need to
            if('name'in args):
                print("name in args")
                user_data.loc[int(args['id']),'name'] = [args['name']]

            # update user's gender if need to
            if('gender'in args):
                user_data.loc[int(args['id']),'gender'] = [args['gender']]
            
            # update user's age if need to
            if('age'in args):
                user_data.loc[int(args['id']),'age'] = [args['age']]

            # save back to CSV
            data.to_csv('./data/patients.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise the userId does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404

if __name__ == '__main__':
    pass