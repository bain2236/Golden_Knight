import pygame, sys, os
from pygame.locals import *
from abc import ABCMeta, abstractmethod



class Enemy(pygame.sprite.Sprite, metaclass=ABCMeta):

    __asset_path = "C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Art/"

    def __init__(self, name=None):
        print("CONSTRUCTING BASE CLASS")
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        if name:
            self.name = name
            print("{0} says: I AM ALIVE!".format(self.name))
        self.__animations = []
        print("finished constructing base class")





    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def display(self):
        pass




