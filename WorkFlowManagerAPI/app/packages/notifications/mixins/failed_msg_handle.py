
from WorkFlowManagerAPI.app.packages.notifications.models.pipeline import Pipeline
class HandleFailedMixin(Pipeline):

    def updateQue(self, data, published_result):
        if published_result is True:
            print "Message Published"
            return True
        else:
            print "Message Failed To Publish"
            self.drafts.put(data)
            return False
