import pygame, sys, os
from pygame.locals import *



class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer

        self.size = {"Height": int(screen_height / 6), "Width": int(screen_width / 8)}
        self.__asset_path = ("C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Art/")
        self.__enemy_path = "/Enemies"
        self.speed = 4
        self.__moving_animation_speed = 1
        self.__moving_animation_counter = 0
        self.rect.width = self.size["Width"]
        self.rect.height = self.size["Height"]
        self.rect.centerx = int(screen_width / 2)
        self.rect.centery = int(screen_height - self.size["Height"])
        self.__animations = []
        self.direction = None
        self.rect = self.__animations[0].get_rect()




    def move(self, key):
        self.__animation_state = "Moving"
        if self.direction == "Left":
            self.rect.centerx = self.rect.centerx - self.speed
            self.direction = "Left"
        elif self.direction == "Right":
            self.rect.centerx = self.rect.centerx + self.speed
            self.direction = "Right"


    def display(self):
        if self.direction == "Right":
            return self.__animate(self.__right_moving_animations, self.__animation_state)
        else:
            return self.__animate(self.__left__moving_animations, self.__animation_state)
    # endregion
    # region Personal Methods


    def __animate(self, animations, animation_state):
        if self.__animation_state == "Idle":
            # increment the tick so animations on happen at certain points
            self.__animation_tick += 1
            # do an animation based on the animation speed
            if self.__animation_tick % self.__idle_animation_speed == 0:
                # print(self.__idle_animation_counter)
                # select a new animation from the list
                self.__idle_animation_counter += 1
                # check to stop list going out of bounds
                if self.__idle_animation_counter > len(animations) - 1:
                    self.__idle_animation_counter = 0
            return pygame.transform.scale(animations[self.__idle_animation_counter],
                                          (self.rect.width, self.rect.height))
        elif self.__animation_state == "Moving":
            # increment the tick so animations on happen at certain points
            self.__animation_tick += 1
            # do an animation based on the animation speed
            if self.__animation_tick % self.__moving_animation_speed == 0:
                # print(self.__idle_animation_counter)
                # select a new animation from the list
                self.__moving_animation_counter += 1
                # check to stop list going out of bounds
                if self.__moving_animation_counter > len(animations) - 1:
                    self.__moving_animation_counter = 0
            return pygame.transform.scale(animations[self.__moving_animation_counter],
                                          (self.rect.width, self.rect.height))


    def __load_animations(self):
        images = None

        # load moving right animations
        for _, _, images in os.walk(self.__asset_path + self.__moving_path):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    print((self.__asset_path + self.__moving_path + image))
                    image = pygame.image.load(
                        os.path.join((self.__asset_path + self.__moving_path + image)))
                    self.__animations.append(image)
    # endregion
    # region Debug methods


    def __update_shape(self):
        """
        Used to create the initial movement mechanics
        :return:
        """
        self.shape = Rect((self.position["x"],
                           self.position["y"]),
                          (
                              self.size["Height"],
                              self.size["Width"]))
    # endregion
