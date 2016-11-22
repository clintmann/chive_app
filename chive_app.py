# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
# import mysql.connector

app = Flask(__name__)
api = Api(app)

# for now,
# we will keep a local object that tracks all of the devices,
# this will be replaced with backend stroage(mongo)

DEVICES = {}


def persist_data(obj):
    # storing local object, replace with mongo code
    global DEVICES
    dn = obj['dn']
    # insert into database < CODE GOES HERE >
    DEVICES[dn] = request.json['attributes']
    print "CURRENT DEVICE LIST IS {}".format(DEVICES)


class getInventory(Resource):
    def post(self):
        global DEVICES
        print request.json
        persist_data(request.json)
        return {"status": "OK"}

    def get(self):
        global DEVICES
        return DEVICES

api.add_resource(getInventory, '/device')

if __name__ == '__main__':
    app.run(debug=False)