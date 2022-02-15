from flask_restful import Resource, reqparse
import pandas as pd


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
        print (list(data))
        if args['id'] in list(data['id']):
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


if __name__ == '__main__':
    print(patients().get())
    print(patients().post())
