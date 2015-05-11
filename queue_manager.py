__author__ = 'root'

import Queue


class QueueManager:

    queue = Queue.Queue()

    def __init__(self):
        print 'init queue manager'

    @staticmethod
    def enqueue(request):
        QueueManager.queue.put(request)

    @staticmethod
    def deque():
        QueueManager.queue.get(True)

    @staticmethod
    def print_val():
        print 'hello print_val method : %s' % QueueManager.queue.qsize()