from Visitor import Visitor

class VisitorCatalog():

    def __init__(self):
        self.Visitors = []

    def AddVisitor(self, name):
        v = Visitor(name)
        self.Visitors.append(v)

    def RemoveVisitor(self, name):
        for v in self.Visitors:
            if v.GetName() == name:
                self.Visitors.remove(v)

    def PrintCatalog(self):
        for v in self.Visitors:
            print(v)            

