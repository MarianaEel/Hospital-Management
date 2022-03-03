from flask import Flask
from flask_restful import Resource, Api, reqparse
from multiprocessing import Process
import os

import module.user_management.patient as patient
import module.user_management.staff as staff

class hospital_db():
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(patient.patients, '/patients')
        self.api.add_resource(staff.staffs, '/staffs')
    # def dbprocess(self):
    #     self.childpr = Process(target=self.dbrun, args=('testdb',))
    #     print('Child process will start.')
    #     self.childpr.start()
    #     self.childpr.join()
    #     print('Child process end.')
    # def dbrun(self, name):
    #     print('Run child process %s (%s)...' % (name, os.getpid()))
    #     db = hospital_db.hospital_db()
    #     db.app.run(debug=True)


if __name__ == '__main__':

    # @app.route('/')
    # def index():
    #     return 'Index Page'

    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World'
    db = hospital_db()
    db.app.run(debug=True)  # run Flask app
    # db.dbprocess()
