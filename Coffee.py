class Coffee():
    def __init__(self, name, id):
        self.ID = id
        self.Name = name
    
    def __str__(self):
        return f'{self.ID} ; {self.Name}'

if  __name__ == '__main__':
    cof = Coffee('Cortado', 1)
    print(cof)       