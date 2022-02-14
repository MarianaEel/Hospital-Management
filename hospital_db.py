from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import requests

import module.user_management.patient as patient
import module.user_management.staff as staff


app = Flask(__name__)
api = Api(app)
api.add_resource(patient.patients, '/patients')
api.add_resource(staff.staffs, '/staffs')


if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(patient.patients, '/patients')
    api.add_resource(staff.staffs, '/staffs')

    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return 'Hello, World'

    app.run()  # run Flask app
