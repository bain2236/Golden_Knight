from enemies.enemy import Enemy
import random, os, pygame

class Small_enemy(Enemy):
    def __init__(self, name=None):
        Enemy.__init__(self, name)
        print("CONSTRUCTING SUB CLASS")
        #print(self.__dict__)
        self.__direction_choice = ["Left", "Right"]
        self.direction = random.choice(self.__direction_choice)
        self.__animation_state = "Moving"
        self.speed = 5
        self.rect = None
        self.__animation_path = "Enemies/small_enemy/"
        #self.__load_animations(super(Small_enemy, self).__asset_path, self.__animation_path)
        #self.rect = self.__animations[0].get_rect()


        print(self.__dict__)


    def move(self):
        if not self.rect:
            self.__load_animations(self.__asset_path, self.__animation_path)
        if self.direction == "Left":
            self.rect.centerx = self.rect.centerx - self.speed

        elif self.direction == "Right":
            self.rect.centerx = self.rect.centerx + self.speed

        #print("my name is {0}, I'm a small enemy moving".format(self.name))
        pass


    def attack(self):
        #print("my name is {0}, I'm a small enemy attacking".format(self.name))
        pass

    def display(self):
        print(self.__dict__)
        if self.direction == "Right":
            return
        elif self.direction == "Left":
            return

    def __load_animations(self, asset_path, object_path):
        print("getting animations from {0}{1}".format(asset_path, object_path))
        images = None
        # load right idle animations
        for _, _, images in os.walk(asset_path + object_path):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    image = pygame.image.load(os.path.join((asset_path + object_path + image)))
                    self.__animations.append(image)
                    self.rect = self.__animation[0].get_rect()
