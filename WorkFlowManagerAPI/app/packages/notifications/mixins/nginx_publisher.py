from WorkFlowManagerAPI.app.packages.notifications.models.pipeline import Pipeline
from WorkFlowManagerAPI import config
import json
import ast
from ws4py.client.geventclient import WebSocketClient

socket_config = {"host": config.push_socket_url}
socket_config['baseUrl'] = "ws://%s/ws/" % socket_config['host']


class NginxPushPublisher(Pipeline):

    def publish(self, data, parsed_data):
        payload = parsed_data
        parsed = json.dumps(payload)
        evald = payload
        try:
            ws = WebSocketClient(socket_config['baseUrl'] + str(evald['pipelineId']), protocols=['http-only', 'chat'])
            ws.connect()
            ws.send(str(parsed))
            ws.close()
            return True
        except Exception as e:
            print e
            return False
