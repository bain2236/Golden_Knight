import pygame, sys, os, math
from pygame.locals import *



class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer

    # region Variables

        self.size = {"Height": int(screen_height / 4), "Width": int(screen_width / 8)}
        # self.shape = Rect((self.position["x"],
        #                   self.position["y"]),
        #                   (
        #                   self.size["Height"],
        #                   self.size["Width"]))


        self.speed = 7
        self.colour = (255, 0, 0)
        self.direction = "Right"
        # animation


        self.__animation_tick = 0


        self.__animation_state = "Idle"
        self.__asset_path = ("C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Art/")
        self.__idle_path_right = ("Golden Knight stand idle breathing/Golden Knight right idle/")
        self.__idle_path_left = ("Golden Knight stand idle breathing/Golden Knight left idle/")
        self.__left_moving_path = ("Golden Knight walking/Golden Knight walking/Golden Knight walk with sword face left/")
        self.__right_moving_path = ("Golden Knight walking/Golden Knight walking/Golden Knight walk with sword face right/")
        self.__left_attacking_path = ("Golden Knight attack/Golden Knight attack 2 slash face left/")
        self.__right_attacking_path = ("Golden Knight attack/Golden Knight attack 2 slash face right/")


        self.__left_attacking_animations = []
        self.__right_attacking_animations = []
        self.__attacking_animations_counter = 0
        self.__atacking_animations_speed = int(math.sqrt(self.speed)/2) if int(math.sqrt(self.speed)/2) > 1 else 1
        self.__right_moving_animations = []
        self.__left__moving_animations = []
        self.__moving_animation_counter = 0
        # how many game ticks before we change our animation
        self.__moving_animation_speed = int(math.sqrt(self.speed)/2) if int(math.sqrt(self.speed)/2) > 1 else 1

        self.__idle_animations_right = []
        self.__idle_animations_left = []
        self.__idle_animation_counter = 0
        # how many game ticks before we change our animation
        self.__idle_animation_speed = 1

        self.__load_animations()
        # endregion


        self.rect = self.__idle_animations_left[0].get_rect()
        self.rect.width = self.size["Width"]
        self.rect.height = self.size["Height"]
        self.rect.centerx = int(screen_width / 2)
        self.rect.centery = int(screen_height - self.size["Height"])
        self.__print_rect()


    def __print_player(self):
        print(self.__dict__)

    def __print_rect(self):
        print("x : {0} y : {1}".format(self.rect.x, self.rect.y))
        print("centerx : {0} centery : {1}".format(self.rect.centerx, self.rect.centery))
        print("center {0}".format(self.rect.center))
        print("top left : {0} top right : {1}".format(self.rect.left, self.rect.right))
        print("top : {0} bottom : {1}".format(self.rect.top, self.rect.bottom))
        print("topleft : {0} bottomright : {1}".format(self.rect.topleft, self.rect.bottomright))
        print("width : {0} height : {1}".format(self.rect.width, self.rect.height))

        #print( self.position["y"])

    # region External methods
    def idle(self):
        #print("Player is idle")
        self.__animation_state = "Idle"

    def move(self, key):
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
        print("setting animation state to attacking")
        self.__animation_state = "Attacking"

      #  print("attacking")
      #  self.__print_player()



    def display(self):
        # print("animation state : {0}".format(self.__animation_state))

        if self.__animation_state == "Idle":
            if self.direction == "Right":
                #print("display function return".format(self.__animate(self.__idle_animations_right, self.__animation_state)))
                return self.__animate(self.__idle_animations_right, self.__animation_state)
            else:
                return self.__animate(self.__idle_animations_left, self.__animation_state)
        elif self.__animation_state == "Moving":
            if self.direction == "Right":
                return self.__animate(self.__right_moving_animations, self.__animation_state)
            else:
                return self.__animate(self.__left__moving_animations, self.__animation_state)
        elif self.__animation_state == "Attacking":
            if self.direction == "Right":
                print("drawing attacks")
                return self.__animate(self.__right_attacking_animations, self.__animation_state)
            else:
                return self.__animate(self.__left_attacking_animations, self.__animation_state)
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
        elif self.__animation_state == "Attacking":
            print("animating the attack")
            # increment the tick so animations on happen at certain points
            self.__animation_tick += 1
            # do an animation based on the animation speed
            if self.__animation_tick % self.__atacking_animations_speed == 0:
                # print(self.__idle_animation_counter)
                # select a new animation from the list
                self.__attacking_animations_counter += 1
                # check to stop list going out of bounds
                if self.__attacking_animations_counter > len(animations) - 1:
                    self.__attacking_animations_counter = 0
            return pygame.transform.scale(animations[self.__attacking_animations_counter],
                                          (self.rect.width, self.rect.height))



    def __load_animations(self):
        images = None
        # load right idle animations
        for _, _, images in os.walk(self.__asset_path + self.__idle_path_right):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    image = pygame.image.load(os.path.join((self.__asset_path + self.__idle_path_right + image)))
                    self.__idle_animations_right.append(image)
        # load left idle animations
        for _, _, images in os.walk(self.__asset_path + self.__idle_path_left):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    image = pygame.image.load(os.path.join((self.__asset_path + self.__idle_path_left + image)))
                    self.__idle_animations_left.append(image)
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
         # load attacking left animations
        for _, _, images in os.walk(self.__asset_path + self.__left_attacking_path):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    image = pygame.image.load(os.path.join((self.__asset_path + self.__left_attacking_path + image)))
                    self.__left_attacking_animations.append(image)
            # load attacking right animations
        for _, _, images in os.walk(self.__asset_path + self.__right_attacking_path):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    image = pygame.image.load(os.path.join((self.__asset_path + self.__right_attacking_path + image)))
                    self.__right_attacking_animations.append(image)


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





