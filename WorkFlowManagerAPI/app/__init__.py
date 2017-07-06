from flask import Flask, render_template, redirect, request
from thoonk import Pubsub

app = Flask(__name__)
# can specify redis host here , meanwhile piggyback on localhost
app._pubsub = Pubsub(listen=False)

from WorkFlowManagerAPI.app.controllers import notification_controller
