from Conversation import Conversation
class ConCatalog():
    def __init__(self):
        self.Conversations = []
        

    def AddCoversation(self, name, txt):
           self.Conversations.append(Conversation(name, txt)) 


    def GetConversations(self):
        return self.Conversations       