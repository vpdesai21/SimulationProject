__author__ = 'root'

import httplib2
import config

http = httplib2.Http()


class MessageUtil:


    @staticmethod
    def set_role(self, role):
        self.role = role

    def __init__(self):
        print 'init Message Util'

    @staticmethod
    def send_message(from_node, to_node, message, action_type):
        # url = config.get_rest_url(to_node)
        url = 'https://developer.yahoo.com/'
        # port = config.get_port(to_node)
        response, content = http.request(url)
        return response.status