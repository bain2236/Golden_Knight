import pygame, sys, os
from pygame.locals import *
from abc import ABCMeta, abstractmethod
from functions import load_animations, animate


class Enemy(pygame.sprite.Sprite, metaclass=ABCMeta):
    """
    abstract super class for the enemies
    """

    def __init__(self, screen_size=None, name=None):
        #print("CONSTRUCTING BASE CLASS")
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        if name:
            self.name = name
        self.size = {"Height": int(screen_size[1] / 20), "Width": int(screen_size[0] / 35)}
        self.animations = []
        self.rect = None
        self.animation_state = None
        self.animation_tick = None
        self.animation_speed = None
        self.moving_animation_counter = None

    def load_animations(self, path_to_enemy_animations):
        """
        calls the helper function to fill up the animation list
        creates the enemy rect
        """
        self.animations = load_animations(self.animations, path_to_enemy_animations)
        self.rect = self.animations[0].get_rect()

    def move(self):
        if self.direction == "Left":
            self.rect.centerx = self.rect.centerx - self.speed
        elif self.direction == "Right":
            self.rect.centerx = self.rect.centerx + self.speed


    @abstractmethod
    def attack(self):
        pass


    def display(self):
        """
        draws the enemy
        :return:
        """
        if self.direction == "Right":
            return self.animate(self.animations, True)
        elif self.direction == "Left":
            return self.animate(self.animations)
        pass

    def animate(self, animations, flip = None):
        """
        same as the players animation function - this should be pulled out into helper functions
        :param animations:
        :param animation_state:
        :return:
        """

        self.moving_animation_counter, self.animation_tick, image = \
            animate(self.animation_tick, self.animation_speed, self.moving_animation_counter, animations)
        if flip:
            image = pygame.transform.flip(image, True, False)
        return pygame.transform.scale(image, (self.rect.width, self.rect.height))






