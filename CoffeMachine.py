from CoffeeMenu import CoffeeMenu

class CoffeMachine():
    def __init__(self, name, model):
        self.Name = name
        self.Model= model
        self.CoffeeMenu = CoffeeMenu()

    def CreateCoffeMenu(self):
        self.CoffeeMenu.AddCoffee('Black Coffee')
        self.CoffeeMenu.AddCoffee('Late')
        self.CoffeeMenu.AddCoffee('Cortado')    
    
    def GetCoffeeMenu(self):
        return self.CoffeeMenu.GetMenu()

    def AddToCoffeeMenu(self, coffee):
        self.CoffeeMenu.AddCoffee(coffee)  

    def EmptyCoffeeMenu(self):
        self.CoffeeMenu.EmptyMenu()      

    def __str__(self):
        return f'Coffe Machine : Name = {self.Name}, Model : {self.Model}'

if __name__ == '__main__':
    #cm = CoffeeMenu()
    #cm.addCoffee('Black Coffee')
    #cm.addCoffee('Late')
    #cm.addCoffee('Cortado') 
    print("*****create coffee machine object and print*******")
    cmach = CoffeMachine("cm1", "Model 1")
    print(cmach)
    input("*****Press enter to print coffee list.***************")
    cmach.CoffeeMenu.printMenu()
    
           
    
    
          