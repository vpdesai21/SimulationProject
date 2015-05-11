from flask import Flask
from flask import request

import inbound_worker
import Counter
from queue_manager import QueueManager
from process_manager import ProcessManager


app = Flask(__name__)


@app.route('/')
def enqueue_request():
    QueueManager.enqueue(request)
    QueueManager.print_val()
    return "SUCCESS"


@app.route('/getCustomerQueueSize')
def get_customer_queue_size_request():
    return Counter.give_queue_size()


def run_server():
    ProcessManager.set_role("CUSTOMER")
    print 'make api call to get customer queue size'
    inbound_worker.start_thread()
    app.run()


if __name__ == '__main__':
    run_server()
