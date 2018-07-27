import pygame, sys, os
from pygame.locals import *
from abc import ABCMeta, abstractmethod



class Enemy(pygame.sprite.Sprite, metaclass=ABCMeta):
    def __init__(self, name=None):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        if name:
            self.name = name
            print("{0} says: I AM ALIVE!".format(self.name))

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass


    def display(self):
        pass

    def __load_animations(self):
        pass


