from datetime import datetime

class Order():
    def __init__(self, visitor, coffee):
        self.Visitor = visitor
        self.Coffee = coffee
        self.TimeStamp = str(datetime.now())

    def __str__(self):
        return f'{self.TimeStamp} {self.Visitor} have ordered {self.Coffee}'