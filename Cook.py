__author__ = 'root'
import Person


class Cook(Person):

    def __init__(self, name, age, gender, mood, speed):
        Person.__init__(self, name, age, gender, "Cook", mood)
        self.speed = speed

    @staticmethod
    def get_order(self):
        print "order received"

    @staticmethod
    def process_order(self):
        print "Order is in process"

    @staticmethod
    def inform_announcer(self):
        print "Order is ready"
