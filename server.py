from flask import request
import gevent
from WorkFlowManagerAPI.app import app


if __name__ == '__main__':
    # Now Start WebServer
    app.run(host = "0.0.0.0", port = 8585, debug= True)
