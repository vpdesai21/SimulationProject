__author__ = 'root'
import Person
import config
import time


class Counter(Person):

    queue_size = 0
    time_to_process_order = 10

    def __init__(self, name, age, gender, mood, greeting, farewell):
        Person.__init__(self, name, age, gender, "Customer", mood)
        self.greeting = greeting
        self.farewell = farewell

    @staticmethod
    def greet_customer(self):
        timeout = Counter.time_to_process_order / config.simulation_time_factor
        print "time out val : %f" % timeout
        time.sleep(timeout)
        print("Hi I am ", self.name, "!!! \n ", self.greeting)

    @staticmethod
    def farewell_customer(self):
        print (self.farewell)

    @staticmethod
    def take_order(self):
        print "Order Received"

    @staticmethod
    def generate_bill(self):
        print "Order processed. \n Your total bill is "

    @staticmethod
    def inform_cook(self):
        print "Process this order "

    @staticmethod
    def give_queue_size(self):
        return self.queue_size