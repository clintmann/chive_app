# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


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
    app.run(debug=False, host='0.0.0.0', port=5000)
