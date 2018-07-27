from enemies.enemy import Enemy

class Big_enemy(Enemy):
    def __int__(self, name=None):
        Enemy.__init__(self, name)

    def move(self):
        #print("my name is {0} I'm a BIG! enemy moving".format(self.name))
        pass


    def attack(self):
        #print("my name is {0} I'm a BIG! enemy ATTACKING".format(self.name))
        pass

    def display(self):
        pass