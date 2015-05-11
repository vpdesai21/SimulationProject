__author__ = 'root'
import Person
class announcer(Person):

    def __init__(self, name, age, gender, mood, speed):
        Person.__init__(self, name, age, gender, "announcer", mood)

    def getOrderToServe(self):
        print "Order Ready"

    def serveOrder(self):
        print "Orange sauce, salsa sauce, Paper napkins added. \n Please collect your order"

