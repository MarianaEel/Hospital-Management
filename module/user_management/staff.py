from flask_restful import Resource, reqparse
import pandas as pd


class staffs(Resource):
    def get(self):
        data = pd.read_csv('./data/staffs.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('gender', required=True)
        parser.add_argument('role', required=True)
        parser.add_argument('title', required=True)
        parser.add_argument('departmentid', required=True)
        parser.add_argument('departmentname', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('./data/staffs.csv')

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
                'role': [args['role']],
                'title': [args['title']],
                'departmentid': [args['departmentid']],
                'departmentname': [args['departmentname']]
            })
            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            # save back to CSV
            data.to_csv('./data/staffs.csv', index=False)
            return {'data': data.to_dict()}, 200  # return data with 200 OK

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add args
        parser.add_argument('name', required=False)
        parser.add_argument('gender', required=False)
        parser.add_argument('role', required=False)
        parser.add_argument('title', required=False)
        parser.add_argument('departmentid', required=False)
        parser.add_argument('departmentname', required=False)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('./data/staffs.csv')

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
            data.to_csv('./data/staffs.csv', index=False)
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
        data = pd.read_csv('./data/staffs.csv')
        
        if int(args['id']) in list(data['id']):
            # remove data entry matching given id
            data = data[data['id'] != int(args['id'])]
            
            # save back to CSV
            data.to_csv('./data/staffs.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        else:
            # otherwise we return 404 because id does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404

