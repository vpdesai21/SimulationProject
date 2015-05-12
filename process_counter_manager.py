__author__ = 'root'


class ProcessManager:

    role = "CUSTOMER"

    @staticmethod
    def set_role(role):
        ProcessManager.role = role

    def __init__(self):
        print 'init Process Manager'

    @staticmethod
    def process_counter_request(request):
        if request.args.get('action') == "GREETING":
            print 'make rest call to customer - greet back'
        elif request.args.get('action') == "ORDER":
            print 'make rest call to customer - for here or to go'
        elif request.args.get('action') == "ORDER_ADDITIONAL_INFO":
            print 'make rest call to customer - payment type'
        elif request.args.get('action') == "ORDER_PAYMENT_INFO":
            print 'process payment'
            print 'if card failure - make rest call to customer - try again'
            print 'if cash - make rest call to customer - give token & change'
            print 'if card success - make rest call to customer - give token - farewell greeting'
            print 'if payment success - make rest call to cook - give order details'
        elif request.args.get('action') == "OTHER_REQUEST":
            print 'make rest call to customer - based on parameters - yes/no'
        elif request.args.get('action') == "RANDOM_MESSAGE":
            print 'make rest call to sender - based on parameters - busy or not'