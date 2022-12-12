import sqlite3

class DBConnection():
    def __init__(self, name):
        self.Con = sqlite3.connect(name)
        self.Cur = self.Con.cursor()
        
    def CreateTable(self):
        self.Cur.execute("CREATE TABLE Coffee (name, price)")
        
    def InsertCoffee(self):
        self.Cur.execute("""INSERT INTO Coffee VALUES ('Late', 20), ('Espresso', 10)""")
        self.Con.commit()
        
if __name__ == '__main__':
    db = DBConnection('CoffeCorne.db')
    #db.CreateTable()
    db.InsertCoffee() 
                