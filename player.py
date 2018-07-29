import pygame, sys, os, math
from pygame.locals import *
from functions import load_animations


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        # call Sprite initializer
        pygame.sprite.Sprite.__init__(self)

    # region VARIABLES

        self.size = {"Height": int(screen_height / 4), "Width": int(screen_width / 8)}
        self.speed = 7
        self.colour = (255, 0, 0)
        self.direction = "Right"
        # animation
        # animation paths
        self.__animation_tick = 0
        self.__animation_state = "Idle"
        self.__idle_path_right = ("Golden Knight stand idle breathing/Golden Knight right idle/")
        self.__idle_path_left = ("Golden Knight stand idle breathing/Golden Knight left idle/")
        self.__left_moving_path = ("Golden Knight walking/Golden Knight walking/Golden Knight walk with sword face left/")
        self.__right_moving_path = ("Golden Knight walking/Golden Knight walking/Golden Knight walk with sword face right/")
        self.__left_attacking_path = ("Golden Knight attack/Golden Knight attack 2 slash face left/")
        self.__right_attacking_path = ("Golden Knight attack/Golden Knight attack 2 slash face right/")

        # animation lists
        self.__left_attacking_animations = []
        self.__right_attacking_animations = []
        self.__right_moving_animations = []
        self.__left__moving_animations = []
        self.__idle_animations_right = []
        self.__idle_animations_left = []

        # animation speeds
        self.__atacking_animations_speed = int(math.sqrt(self.speed) / 2) if int(math.sqrt(self.speed) / 2) > 1 else 1
        self.__moving_animation_speed = int(math.sqrt(self.speed) / 2) if int(math.sqrt(self.speed) / 2) > 1 else 1
        self.__idle_animation_speed = 1

        # animation counters - to track which image we should be showing at any time
        self.__attacking_animations_counter = 0
        self.__moving_animation_counter = 0
        self.__idle_animation_counter = 0

        # dynamically fill all of our animation lists from the paths above.
        self.__load_animations()

        # use an animation image to get the rect of the sprite
        self.rect = self.__idle_animations_left[0].get_rect()
        # set size and position of sprite based on screen size. (this needs a bit more work so player always appears
        # in the correct position on the ground)
        self.rect.width = self.size["Width"]
        self.rect.height = self.size["Height"]
        self.rect.centerx = int(screen_width / 2)
        self.rect.centery = int(screen_height - self.size["Height"])
#        self.__print_rect()

        # endregion

    # region PUBLIC FUNCTIONS

    def idle(self):
        """
        Default state when player is not doing anything
        :return:
        """
        self.__animation_state = "Idle"

    def move(self, key):
        """
        Handles moving of the player
        :param key: the key pressed by the user
        :return:
        """
        self.__animation_state = "Moving"
        if key == pygame.K_LEFT:
            self.rect.centerx = self.rect.centerx - self.speed
            self.direction = "Left"
        elif key == pygame.K_RIGHT:
            self.rect.centerx = self.rect.centerx + self.speed
            self.direction = "Right"
        else:
            self.__animation_state = "Idle"

    def attack(self):
        """
        Called when the user hits the attack button
        :return:
        """
        self.__animation_state = "Attacking"

    def display(self):
        """
        Calls the animate function based on direction/state
        :return: A scaled image and the players height and width
        """
        # animate the player when it's idle
        if self.__animation_state == "Idle":
            if self.direction == "Right":
                return self.__animate(self.__idle_animations_right, self.__animation_state)
            else:
                return self.__animate(self.__idle_animations_left, self.__animation_state)
        # animate the player when it's moving
        elif self.__animation_state == "Moving":
            if self.direction == "Right":
                return self.__animate(self.__right_moving_animations, self.__animation_state)
            else:
                return self.__animate(self.__left__moving_animations, self.__animation_state)
        # animate the player when it's attacking
        elif self.__animation_state == "Attacking":
            if self.direction == "Right":
                return self.__animate(self.__right_attacking_animations, self.__animation_state)
            else:
                return self.__animate(self.__left_attacking_animations, self.__animation_state)

    # endregion

    # region PRIVATE FUNCTIONS
    def __animate(self, animations, animation_state):
        """
        selects images from the animation lists based on animation speed
        :param animations: a list of images
        :param animation_state: the current state of the player
        :return: A scaled image from the list and the players height and width
        """

        #todo extract this function into helper functions and pass in the variables required.

        if self.__animation_state == "Idle":
            # increment the tick so animations happen at certain points - this the same as the game tick
            self.__animation_tick += 1
            # change the image to the next in the list
            if self.__animation_tick % self.__idle_animation_speed == 0:
                self.__idle_animation_counter += 1
                # handle list out of bounds and reset the counter and tick
                if self.__idle_animation_counter > len(animations) - 1:
                    self.__idle_animation_counter = 0
                    self.__animation_tick = 0
            return pygame.transform.scale(animations[self.__idle_animation_counter],
                                          (self.rect.width, self.rect.height))
        elif self.__animation_state == "Moving":
            # increment the tick so animations happen at certain points - this the same as the game tick
            self.__animation_tick += 1
            # change the image to the next in the list
            if self.__animation_tick % self.__moving_animation_speed == 0:
                self.__moving_animation_counter += 1
                # handle list out of bounds and reset the counter and tick
                if self.__moving_animation_counter > len(animations) - 1:
                    self.__moving_animation_counter = 0
                    self.__animation_tick = 0
            return pygame.transform.scale(animations[self.__moving_animation_counter],
                                          (self.rect.width, self.rect.height))
        elif self.__animation_state == "Attacking":
            print("animating the attack")
            # increment the tick so animations happen at certain points - this the same as the game tick
            self.__animation_tick += 1
            # change the image to the next in the list
            if self.__animation_tick % self.__atacking_animations_speed == 0:
                self.__attacking_animations_counter += 1
                # handle list out of bounds and reset the counter and tick
                if self.__attacking_animations_counter > len(animations) - 1:
                    self.__attacking_animations_counter = 0
                    self.__animation_tick = 0
            return pygame.transform.scale(animations[self.__attacking_animations_counter],
                                          (self.rect.width, self.rect.height))



    def __load_animations(self):
        """
        Calls the helper function load_animations which fills an animation list
        :return:
        """
        self.__idle_animations_right = load_animations(self.__idle_animations_right, self.__idle_path_right)
        self.__idle_animations_left = load_animations(self.__idle_animations_left, self.__idle_path_left)
        self.__right_moving_animations = load_animations(self.__right_moving_animations, self.__right_moving_path)
        self.__left__moving_animations = load_animations(self.__left__moving_animations, self.__left_moving_path)
        self.__left_attacking_animations = load_animations(self.__left_attacking_animations, self.__left_attacking_path)
        self.__right_attacking_animations = load_animations(self.__right_attacking_animations, self.__right_attacking_path)
    # endregion

    # region DEBUG FUNCTIONS
    def __update_shape(self):
        """
        Used for debugging
        :return:
        """
        self.shape = Rect((self.position["x"],
                           self.position["y"]),
                          (
                           self.size["Height"],
                           self.size["Width"]))

        def __print_player(self):
            """
            Used for debugging
            :return:
            """
            print(self.__dict__)

        def __print_rect(self):
            """
            Used for debugging
            :return:
            """
            print("x : {0} y : {1}".format(self.rect.x, self.rect.y))
            print("centerx : {0} centery : {1}".format(self.rect.centerx, self.rect.centery))
            print("center {0}".format(self.rect.center))
            print("top left : {0} top right : {1}".format(self.rect.left, self.rect.right))
            print("top : {0} bottom : {1}".format(self.rect.top, self.rect.bottom))
            print("topleft : {0} bottomright : {1}".format(self.rect.topleft, self.rect.bottomright))
            print("width : {0} height : {1}".format(self.rect.width, self.rect.height))

    # endregion





