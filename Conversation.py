class Conversation():
    def __init__(self, name, txt):
        self.Name=name
        self.Text= txt

    def __str__(self):
        return f' {self.Name} writes: {self.Text}'    
