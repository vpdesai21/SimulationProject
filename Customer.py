__author__ = 'root'
import Person

class Customer(Person):

    def __init__(self, name, age, gender, mood, money, isHungry, patience):
        Person.__init__(self, name , age, gender, "Customer", mood)
        self.money = money
        self.isHungry = isHungry
        self.patience = patience

    def giveOrder(self):
        print("I want XYZ ")

    def observeQueue(self):
        print "How many people are there in queue? Should I wait or should I leave?"

    def checkMenu(self):
        print "What should I eat ??"

    def checkMoney(self):
        print "How much $ are there in my pocket?? "

    def waitInQueue(self):
        print "Waiting in queue"

    def collectFood(self):
        print "Finally I got my food"

    def getAdditinalItem(self,item):
        print "I want some more ", item




