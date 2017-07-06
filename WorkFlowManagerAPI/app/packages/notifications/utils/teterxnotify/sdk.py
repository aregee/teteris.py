from gevent import Greenlet
from WorkFlowManagerAPI import config
from requests.auth import HTTPBasicAuth
import requests
import json

notification_url = config.push_socket_url

auth = HTTPBasicAuth(config.socket_api_user, config.socket_api_key)


class TeterXnotify(Greenlet):

    """
        notify = TeterXnotify()
        notify.publish(client_id='3d91928b729b432ca22799cb909e2f1d',
                   author='3d91928b729b432ca22799cb909e2f1f',
                   message='HEllo Random %s!' % x, channel='franklyMe')
    """

    def __init__(self, notify_to=None, message=None):
        self.client_id = notify_to
        self.message = message
        # get user credentials

    @staticmethod
    def publish(data, client_id):
        payload = {"message": data, "client_id": client_id}
        r = requests.post(notification_url, data=json.dumps(payload), headers={'content-type': 'application/json'})

        if r.status_code == requests.codes.ok:
            print(r.headers['content-type'])
            return True
        else:
            print r.headers
            return r.status_code
