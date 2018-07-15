import pygame, sys, os
from pygame.locals import *



class Player:
    def __init__(self):

    # region Variables
        self.position = {"x": -20, "y": -20}
        self.size = {"Height": 20, "Width": 20}
        self.shape = Rect((self.position["x"],
                          self.position["y"]),
                          (
                          self.size["Height"],
                          self.size["Width"]))
        self.speed = 3
        self.colour = (255, 0, 0)
        self.direction = "Right"
        # animation


        self.__animation_tick = 0

        self.__animation_state = "Idle"
        self.__asset_path = ("C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Art/")
        self.__idle_path = ("Golden Knight stand idle breathing/Golden Knight right idle/")
        self.__left_moving_path = ("Golden Knight walking/Golden Knight walking/Golden Knight walk with sword face left/")
        self.__right_moving_path= ("Golden Knight walking/Golden Knight walking/Golden Knight walk with sword face right/")

        self.__right_moving_animations = []
        self.__left__moving_animations = []
        self.__moving_animation_counter = 0
        self.__moving_animation_speed = 3

        self.__idle_animations = []
        self.__idle_animation_counter = 0
        self.__idle_animation_speed = 4

        self.__load_animations()
        # endregion

    # region External methods
    def idle(self):
        print("Player is idle")
        self.__animation_state = "Idle"

    def move(self, key):
        self.__animation_state = "Moving"
        if key == pygame.K_LEFT:
            self.position["x"] = self.position["x"] - self.speed
            self.direction = "Left"
        elif key == pygame.K_RIGHT:
            self.position["x"] = self.position["x"] + self.speed
            self.direction = "Right"
        else:
            self.__animation_state = "Idle"



    def display(self):
        print("animation state : {0}".format(self.__animation_state))
        if self.__animation_state == "Idle":
            if self.direction == "Right":
                return self.__animate(self.__idle_animations, self.__animation_state)
            else:
                image = self.__animate(self.__idle_animations, self.__animation_state)
                return pygame.transform.flip(image, True, False)
        elif self.__animation_state == "Moving":
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
                #print(self.__idle_animation_counter)
                # select a new animation from the list
                self.__idle_animation_counter += 1
                # check to stop list going out of bounds
                if self.__idle_animation_counter > len(animations) - 1:
                    self.__idle_animation_counter = 0
            return animations[self.__idle_animation_counter]
        elif self.__animation_state == "Moving":
            # increment the tick so animations on happen at certain points
            self.__animation_tick += 1
            # do an animation based on the animation speed
            if self.__animation_tick % self.__moving_animation_speed == 0:
                #print(self.__idle_animation_counter)
                # select a new animation from the list
                self.__moving_animation_counter += 1
                # check to stop list going out of bounds
                if self.__moving_animation_counter > len(animations) - 1:
                    self.__moving_animation_counter = 0
            return animations[self.__moving_animation_counter]


    def __load_animations(self):
        images = None
        # load idle animations
        for _, _, images in os.walk(self.__asset_path + self.__idle_path):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    image = pygame.image.load(os.path.join((self.__asset_path + self.__idle_path + image)))
                    self.__idle_animations.append(image)
        # load moving right animations
        for _, _, images in os.walk(self.__asset_path + self.__right_moving_path):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    print((self.__asset_path + self.__right_moving_path + image))
                    image = pygame.image.load(os.path.join((self.__asset_path + self.__right_moving_path + image)))
                    self.__right_moving_animations.append(image)
        # load moving left animations
        for _, _, images in os.walk(self.__asset_path + self.__left_moving_path):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    image = pygame.image.load(os.path.join((self.__asset_path + self.__left_moving_path + image)))
                    self.__left__moving_animations.append(image)


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





