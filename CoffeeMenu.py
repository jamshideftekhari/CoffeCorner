from Coffee import Coffee 
from CoffeeRepo import CoffeeRepo

class CoffeeMenu():
    def __init__(self):
        self.Repo = CoffeeRepo()
        self.Repo.ReadCSV()
        self.Menu = self.Repo.GetCoffeeList()

    def AddCoffee(self, name):
        id = self.Repo.GetCoffeeId()
        cof = Coffee(name, id)
        self.Repo.AddCoffee(cof)
        self.Repo.SaveToCsv()    

    def EmptyMenu(self):
        self.Repo.EmptyCoffeeList()
        self.Repo.SaveToCsv()
    
    def printMenu(self):
        for c in self.Menu:
            print(c)
   
    def GetMenu(self):
        return self.Menu


if __name__ == '__main__':
    cm = CoffeeMenu()
    cm.printMenu()
    cm.AddCoffee('Espresso')
    cm.printMenu()
    cm.Repo.SaveToCsv()  
        