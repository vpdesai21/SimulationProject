__author__ = 'root'
import Person


class Customer(Person):

    def __init__(self, name, age, gender, mood, money, isHungry, patience):
        Person.__init__(self, name , age, gender, "Customer", mood)
        self.money = money
        self.isHungry = isHungry
        self.patience = patience

    @staticmethod
    def give_order(self):
        print("I want XYZ ")

    @staticmethod
    def observe_queue(self):
        print "How many people are there in queue? Should I wait or should I leave?"

    @staticmethod
    def check_menu(self):
        print "What should I eat ??"

    @staticmethod
    def check_money(self):
        print "How much $ are there in my pocket?? "

    @staticmethod
    def wait_in_queue(self):
        print "Waiting in queue"

    @staticmethod
    def collect_food(self):
        print "Finally I got my food"

    @staticmethod
    def get_additional_item(self,item):
        print "I want some more ", item