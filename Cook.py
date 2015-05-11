__author__ = 'root'
import Person

class Cook(Person):

    def __init__(self, name, age, gender, mood, speed):
        Person.__init__(self, name, age, gender, "Cook", mood)
        self.speed = speed

    def getOrder(self):
        print "order received"

    def processOrder(self):
        print "Order is in process"

    def informAnnouncer(self):
        print "Order is ready"
