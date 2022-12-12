from Order import Order
class OrderCatalog():
    def __init__(self):
        self.Orders=[]

    def AddOrder(self, name, coffee):
        order = Order(name, coffee)
        self.Orders.append(order)

    def RemoveOrder(self,index):
        pass

    def GetOrderList(self):
        return self.Orders