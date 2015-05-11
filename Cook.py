__author__ = 'root'
import Person
import config
import time


class Cook(Person):

    def __init__(self, name, age, gender, mood, speed):
        Person.__init__(self, name, age, gender, "Cook", mood)
        self.speed = speed

    @staticmethod
    def get_order(self,order):
        print "New Order Received"
        #check if this is right
        self.process_order(self,order)


    @staticmethod
    def process_order(self,order):
        timeout = 30 / config.simulation_time_factor
        time.sleep(timeout)
        print "Order Ready"
        self.inform_announcer(self,order)

    @staticmethod
    def inform_announcer(self,order):
        time.sleep(10)
        print "Order is ready"

