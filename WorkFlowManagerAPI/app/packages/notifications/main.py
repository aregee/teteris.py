import gevent
import os
from mixins import JSONParserMixin, ThoonkQeueParserMixin, HTTPPublisher
import multiprocessing
import gipc


class AsyncNotifyPublisher(JSONParserMixin, ThoonkQeueParserMixin, HTTPPublisher):
    def handle(self, data):
        print "handling notification data"
        parsed_data = self.parse(data)
        published_result = self.publish(data, parsed_data)
        print published_result

def process_start():
    print "starting processing"
    print "==================="
    print os.getpid()
    notify_workers = [AsyncNotifyPublisher(x, 'notify') for x in xrange(1, 100)]
    spawn_all = notify_workers
    for worker in spawn_all:
        worker.start()
    gevent.joinall(spawn_all)


def run_workers(target):
    """
    Creates processes * <limit>, running the given target
    function for each.
    """
    limit = multiprocessing.cpu_count() / 2
    for _ in range(limit):
        proc = gipc.start_process(target)
        proc.join()

if __name__ == '__main__':
    process_start()
