__author__ = 'root'

class ProcessManagerCook:

    role = "COOK"

    @staticmethod
    def set_role(self, role):
        self.role = role

    def __init__(self):
        print 'Cook Process Manager'

    @staticmethod
    def process_new_order_request(request):
        if request.args.get('action') == "NEWORDER":
            print 'make rest call to get order in Cook.py'
