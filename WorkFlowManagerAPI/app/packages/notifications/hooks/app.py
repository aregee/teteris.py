from flask import Flask, request, jsonify
from functools import wraps
import json
from WorkFlowManagerAPI.app import app as workflow_app
from WorkFlowManagerAPI import config
import gevent


def check_auth(username, password):
    return username == config.socket_api_user and password == config.socket_api_key


def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


def add_to_tetrx(data, queue):
    j = workflow_app._pubsub.queue(queue)
    data = json.dumps(data)
    j.put(str(data))
    return True


def process_data(data, queue):
    publisher = gevent.spawn(add_to_tetrx, data, queue)
    gevent.joinall([publisher])
    return publisher
