__author__ = 'root'
import Person

class Counter(Person):

    def __init__(self, name, age, gender, mood, greeting, farewell):
        Person.__init__(self, name, age, gender, "Customer", mood)
        self.greeting = greeting
        self.farewell = farewell

    def greetCustomer(self):
        print("Hi I am ", self.name, "!!! \n ", self.greeting)

    def farewellCustomer(self):
        print (self.farewell)

    def takeOrder(self):
        print "Order Received"

    def generateBill(self):
        print "Order processed. \n Your total bill is "

    def informCook(self):
        print "Process this order "





