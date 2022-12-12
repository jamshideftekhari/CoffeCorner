from VisitorCataloge import VisitorCatalog
from CoffeMachine import CoffeMachine
from ConCatalog import ConCatalog
from OrderCatalog import OrderCatalog

class CoffeeCorner():
    def __init__(self, name, adress):
        self.Name = name
        self.Adress = adress
        self.Visitors = VisitorCatalog()
        self.CM = CoffeMachine('aa','dd')
        self.CL = ConCatalog()
        self.OL = OrderCatalog()
        

    def RegisterUser(self, name):
        VisitorCatalog.AddVisitor(name)

    def AddOrder(self, name, coffee):
        self.OL.AddOrder(name, coffee)
    
    def GetOrderList(self):
        return self.OL.GetOrderList()

    def PrintCoffeeMenu(self):
        self.CM.CreateCoffeMenu()
        self.CM.CoffeeMenu.printMenu()

    def GetChatList(self):
        return self.CL.GetConversations()

    def AddToChatList(self, name, txt):
        self.CL.AddCoversation(name,txt)


    def PrinUsers():
        pass    

if __name__ == '__main__':
    cc = CoffeeCorner('Corner1', 'A3')
    cc.PrintCoffeeMenu()
