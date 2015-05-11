__author__ = 'root'
import Person


class Announcer(Person):

    def __init__(self, name, age, gender, mood, speed):
        Person.__init__(self, name, age, gender, "announcer", mood)

    @staticmethod
    def get_order_to_serve(self):
        print "Order Ready"

    @staticmethod
    def serve_order(self):
        print "Orange sauce, salsa sauce, Paper napkins added. \n Please collect your order"

