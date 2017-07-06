import sys
import time
import gevent
from gevent import Greenlet
from WorkFlowManagerAPI.app import app

class Pipeline(gevent.Greenlet):

    def __init__(self, name, queue):
        # listen to thoonk qeue list here
        self.ps_all = time.time()
        self.queue = queue
        self.inbox = app._pubsub.queue(self.queue)
        self.drafts = app._pubsub.queue('backlogs')
        self.name = name
        Greenlet.__init__(self)

    def receive(self, name, task):

        print("Worker %s recived task %s" % (name, task))

    def handle(self, data):

        raise NotImplemented('No handle Mixin')

    def _run(self):
        self.running = True

        while self.running:
            try:
                while True:
                    # decrements queue size by
                    task = self.inbox.get(timeout=1)
                    print('Worker %s got task %s' % (self.name, task))
                    ts = time.time()
                    print "invoking:"
                    try:
                        self.handle(task)
                    except Exception as e:
                        print "should have handled"
                        print e

                    gevent.sleep(1)
                    # print job.result
                    print('Took {}s'.format(time.time() - ts))
            except Exception as e:
                print e
                pass
            except KeyboardInterrupt:
                sys.exit(['Closing notification system now'])
