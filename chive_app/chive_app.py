# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app, version='1.0', title='CHIVE API', default='CHIVE', default_label='CHIVE namespace', description='CHIVE API is a simple API to GET DN information for objects in a Cisco ACI Fabric')


# for now,
# we will keep a local object that tracks all of the devices,
# this will be replaced with backend storage(mongo)

DEVICES = {}


def persist_data(obj):
    # storing local object, replace with mongo code
    global DEVICES
    dn = obj['dn']
    # insert into database < CODE GOES HERE >
    DEVICES[dn] = request.json['attributes']
    print "CURRENT DEVICE LIST IS {}".format(DEVICES)


# Decorate your operation
@api.route('/device')
class getInventory(Resource):

    def post(self):
        global DEVICES
        print request.json
        persist_data(request.json)
        return {"status": "OK"}

    def get(self):
        global DEVICES
        return DEVICES

if __name__ == '__main__':
    app.run(debug=True)

