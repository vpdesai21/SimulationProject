__author__ = 'root'


class ProcessManager:

    role = "CUSTOMER"

    @staticmethod
    def set_role(self, role):
        self.role = role

    def __init__(self):
        print 'init Process Manager'

    @staticmethod
    def process_customer_request(request):
        if request.args.get('action') == "GREETING":
            print 'make rest call to greet back'


    @staticmethod
    def process_counter_request(request):
        if request.args.get('action') == "GREETING":
            print 'make rest call to ask for order'