from flask_restful import Resource
import pandas as pd


class staffs(Resource):
    def get(self):
        data = pd.read_csv('./data/staffs.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

    

    def add_staff(name: str, gender: str, role: str, title: str, department_id: int, department_name: str):
        pass
