import pygame, sys, os
from pygame.locals import *
from abc import ABCMeta, abstractmethod
from functions import load_animations


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

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass


    def display(self):
        """
        draws the enemy
        :return:
        """
        if self.direction == "Right":
            return self.animate(self.animations, self.animation_state, True)
        elif self.direction == "Left":
            return self.animate(self.animations, self.animation_state)
        pass

    def animate(self, animations, animation_state, flip = None):
        """
        same as the players animation function - this should be pulled out into helper functions
        :param animations:
        :param animation_state:
        :return:
        """
        if animation_state == "Moving":
            # increment the tick so animations on happen at certain points
            self.animation_tick += 1
            # do an animation based on the animation speed
            if self.animation_tick % self.animation_speed == 0:
                # print(self.__idle_animation_counter)
                # select a new animation from the list
                self.moving_animation_counter += 1
                # check to stop list going out of bounds
                if self.moving_animation_counter > len(animations) - 1:
                    self.moving_animation_counter = 0
                    self.animation_tick = 0

            if not flip:
                return pygame.transform.scale(animations[self.moving_animation_counter],
                                          (self.rect.width, self.rect.height))
            # flips the sprite to face the opposite direction
            elif flip:
                return pygame.transform.scale(pygame.transform.flip(animations[self.moving_animation_counter], True, False),
                                              (self.rect.width, self.rect.height))




