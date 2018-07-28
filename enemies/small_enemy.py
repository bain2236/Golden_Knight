from enemies.enemy import Enemy
import random, os, pygame
from functions import load_animations


class Small_enemy(Enemy):
    def __init__(self,  screen_size=None, name=None):

        super().__init__(screen_size,name)

        # enemies specific animation folder
        self.__animation_path = "Enemies/small_enemy/"
        # randomly choose a direction to face
        self.__direction_choice = ["Left", "Right"]
        self.direction = random.choice(self.__direction_choice)

        self.speed = 5
        self.rect = None
        # load animations and set animation variables
        self.load_animations(self.__animation_path)
        self.animation_state = "Moving"
        self.animation_tick = 0
        self.animation_speed = 5
        self.moving_animation_counter = 0

        # resize the sprite
        self.rect.width = self.size["Width"]
        self.rect.height = self.size["Height"]

        if self.direction == "Left":
            self.rect.centerx = screen_size[0] + self.rect.width
            self.rect.centery = screen_size[1] - self.size["Height"]*3 - 3
        elif self.direction == "Right":
            self.rect.centerx = 0 - self.rect.width
            self.rect.centery = screen_size[1] - self.size["Height"]*3 - 5
        # used for debugging
        print("{0} says: I AM ALIVE! -- {1}".format(self.name, self.__dict__))


    def move(self):
        if self.direction == "Left":
            self.rect.centerx = self.rect.centerx - self.speed
        elif self.direction == "Right":
            self.rect.centerx = self.rect.centerx + self.speed

        #print("my name is {0}, I'm a small enemy moving".format(self.name))
        pass


    def attack(self):
        #print("my name is {0}, I'm a small enemy attacking".format(self.name))
        pass


