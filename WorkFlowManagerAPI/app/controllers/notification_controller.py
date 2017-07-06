import json
from flask import request

from WorkFlowManagerAPI.app import app
from WorkFlowManagerAPI.app.packages.notifications import process_data

# exposing api to add notification message object to q
@app.route('/publish/notifications', methods=['POST'])
def api_notify():
    from flask import jsonify
    if request.headers['Content-Type'] == 'application/json':
        # add message to que here
        # check if message contains notify_to and notification_from fields here
        if request.json:
            data = request.json
            ret_val = process_data(data, 'notify')
            print ret_val
            return jsonify(request.json)
        resp = jsonify(
            {"message": "Bad Request!"}), 403, 'application/json'
        return resp
    else:
        resp = jsonify(
            {"message": "Bad Request!"}), 403, 'application/json'
        return resp
