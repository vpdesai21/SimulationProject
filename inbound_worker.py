__author__ = 'root'

import logging
import threading
import time
from process_manager import ProcessManager
from queue_manager import QueueManager


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


def worker():
    logging.debug('Starting worker')
    while True:
        QueueManager.print_val()
        req = QueueManager.deque()
        time.sleep(10)
        to_message = req.args.get('to')
        if to_message == "COUNTER":
            ProcessManager.process_counter_request(req)
        elif to_message == "CUSTOMER":
            ProcessManager.process_customer_request(req)
        elif to_message == "COOK":
            ProcessManager.process_cook_request(req)
        elif to_message == "ANNOUNCER":
            ProcessManager.process_announcer_request(req)
    logging.debug('Exiting worker')


def start_thread():
    w = threading.Thread(name='worker', target=worker)
    w.start()
