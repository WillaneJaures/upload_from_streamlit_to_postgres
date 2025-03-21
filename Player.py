class Player:
    def __init__(self,name,health, attack1, attack2 ):
        self.name = name
        self.health = health
        self.attack1 = attack1
        self.attack2 = attack2
    

    #getter

    def get_name(self):
        return self.name
        
    def get_health(self):
        return self.health
    
    def get_attack1(self):
        return self.attack1
    
    def get_attack2(self):
        return self.attack2
    

    #setter
    
