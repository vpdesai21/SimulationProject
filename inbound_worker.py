__author__ = 'root'

import logging
import threading
from process_manager import ProcessManager

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


def worker():
    logging.debug('Starting worker')

    logging.debug('Exiting worker')


def start_thread():
    ProcessManager.__init__()
    w = threading.Thread(name='worker', target=worker)
    w.start()
