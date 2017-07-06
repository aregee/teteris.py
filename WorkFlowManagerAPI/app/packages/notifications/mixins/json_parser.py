from WorkFlowManagerAPI.app.packages.notifications.models.pipeline import Pipeline
import json

class JSONParserMixin(Pipeline):

    def parse(self, data):
        return json.loads(data)
