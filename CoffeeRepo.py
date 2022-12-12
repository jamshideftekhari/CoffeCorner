from Coffee import Coffee
import csv

class CoffeeRepo():
    CoffeeCSV = "CoffeeCsv.csv"
    def __init__(self):
        self.CoffeeList = []
    
    def MakeTestContent(self):
        self.CoffeeList.append(Coffee('Black coffee', 1))
        self.CoffeeList.append(Coffee('Coffee late', 2))
        self.CoffeeList.append(Coffee('Cortado', 3))
 
    def ReadCSV(self):
        with open(self.CoffeeCSV) as repo:
            r = csv.reader(repo, delimiter=';')
            count = 0
            for row in r:
                #print(f' {row[0]} {row[1]}')
                if count>0:
                    self.CoffeeList.append(Coffee(row[1],row[0]))
                count+=1    

    def SaveToCsv(self):
        with open(self.CoffeeCSV, 'w', newline='') as repo:
            w = csv.writer(repo, delimiter=';')
            w.writerow(['Number', 'Name'])
            for c in self.CoffeeList:
                w.writerow([c.ID, c.Name])
    
    def GetCoffeeList(self):
        return self.CoffeeList

    def AddCoffee(self, coffee):
        self.CoffeeList.append(coffee)    
    
    def GetCoffeeId(self):
        return len(self.CoffeeList)

    def EmptyCoffeeList(self):
        self.CoffeeList.clear()
        return self.GetCoffeeId()   
    

if __name__ == '__main__':
    cp = CoffeeRepo()
    cp.MakeTestContent()
    cp.SaveToCsv()
    cp.ReadCSV()


