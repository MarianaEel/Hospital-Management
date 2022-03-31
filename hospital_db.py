import json
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
import pymongo
from module.database_api import mongo_api

import module.user_management.management_factory as factory


class hospital_db():
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(factory.patients, "/patients")
        self.api.add_resource(factory.staffs, "/staffs")
        self.api.add_resource(factory.datas, "/datas")
        self.api.add_resource(factory.chats, "/chats")

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
    db = hospital_db()

    @db.app.route('/')
    def index():
        return render_template('Default.htm')

    @db.app.route('/hello')
    def hello():
        return 'Hello, World'

    @db.app.route('/DeveloperSite')
    def DeveloperSite():
        return render_template('Developer.html')

    db.app.run(host="0.0.0.0", port=8000, debug=True)  # run Flask app
    # db.app.run(port=8000, debug=True)
    # db.dbprocess()
