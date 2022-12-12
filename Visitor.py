from ConCatalog import ConCatalog
from Conversation import Conversation
class Visitor():
    def __init__(self, name):
        self.Name = name
        self.Comments=[] 
    
    def GetName(self):
        return self.Name

    def AddConversation(self, text):
        self.Comments.append(Conversation(text))

    def GetComments(self):
        return self.Comments    

    def __str__(self):
        return f' visitor : {self.Name} says {self.comments[self.Comments.count()-1]}'
             
