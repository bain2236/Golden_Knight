from enemies.enemy import Enemy
import random, os, pygame

# todo complete big enemy much like the small enemy implementation


class Big_enemy(Enemy):
    def __init__(self, screen_size=None, name=None):
        super().__init__(screen_size, name)

        # enemies specific animation folder
        self.__animation_path = "Enemies/big_enemy/"
        # randomly choose a direction to face
        self.direction_choice = ["Left", "Right"]
        self.direction = random.choice(self.direction_choice)

        self.speed = random.randint(1,3)
        self.rect = None
        # load animations and set animation variables
        self.load_animations(self.__animation_path)
        self.animation_state = "Moving"
        self.animation_tick = 0
        self.animation_speed = self.speed
        self.moving_animation_counter = 0

        # resize the sprite
        self.rect.width = self.size["Width"] + 50
        self.rect.height = self.size["Height"] + 50

        if self.direction == "Left":
            self.rect.centerx = screen_size[0] + self.rect.width
            self.rect.centery = screen_size[1] - self.size["Height"] * 3 - 20
        elif self.direction == "Right":
            self.rect.centerx = 0 - self.rect.width
            self.rect.centery = screen_size[1] - self.size["Height"] * 3 - 20
        # used for debugging
        print("{0} says: I AM ALIVE! -- {1}".format(self.name, self.__dict__))

    def attack(self):
        #print("my name is {0} I'm a BIG! enemy ATTACKING".format(self.name))
        pass
