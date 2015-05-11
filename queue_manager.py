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
    def deque(request):
        QueueManager.queue.get()

    @staticmethod
    def print_val():
        print 'hello sys method'