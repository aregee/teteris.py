import ConfigParser
import os
from ast import literal_eval

config_parser = ConfigParser.RawConfigParser()
config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'settings.conf')
config_parser.readfp(open(config_file))

mongo_credentials = literal_eval(config_parser.get('workflowmanager', 'mongo_credentials'))
redis_credentials = literal_eval(config_parser.get('workflowmanager', 'redis_credentials'))
push_socket_url = literal_eval(config_parser.get('workflowmanager', 'socket_url'))
socket_api_user = literal_eval(config_parser.get('workflowmanager', 'socket_api_user'))
socket_api_key = literal_eval(config_parser.get('workflowmanager', 'socket_api_key'))
