from flask import Flask
from flask import request

import inbound_worker
from queue_manager import QueueManager

app = Flask(__name__)


@app.route('/')
def enqueue_request():
    QueueManager.enqueue(request)
    return "SUCCESS"


def run_server():
    app.run()
    QueueManager.__init__()
    inbound_worker.start_thread()


if __name__ == '__main__':
    run_server()
