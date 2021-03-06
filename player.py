import pygame, sys, os, math
from pygame.locals import *
from functions import load_animations, animate


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        # call Sprite initializer
        pygame.sprite.Sprite.__init__(self)

    # region VARIABLES

        self.max_health = 100
        self.current_health = 100
        self.damage = 1000
        self.died = False
        self.size = {"Height": 220, "Width": 280}
        self.speed = 7
        self.colour = (255, 0, 0)
        self.direction = "Right"
        # animation
        # animation paths
        self.__animation_tick = 0
        self.state = "Idle"
        self.__idle_path_right = ("Golden Knight stand idle breathing/Golden Knight right idle/")
        self.__idle_path_left = ("Golden Knight stand idle breathing/Golden Knight left idle/")
        self.__left_moving_path = ("Golden Knight walking/Golden Knight walking/Golden Knight walk with sword face left/")
        self.__right_moving_path = ("Golden Knight walking/Golden Knight walking/Golden Knight walk with sword face right/")
        self.__left_attacking_path = ("Golden Knight attack/Golden Knight attack 2 slash face left/")
        self.__right_attacking_path = ("Golden Knight attack/Golden Knight attack 2 slash face right/")
        self.__left_dead_path = ("Golden Knight died/Golden Knight died face left with sword/")
        self.__right_dead_path = ("Golden Knight died/Golden Knight died face right with sword/")

        # animation lists
        self.__left_attacking_animations = []
        self.__right_attacking_animations = []
        self.__right_moving_animations = []
        self.__left__moving_animations = []
        self.__right_idle_animations = []
        self.__left_idle_animations= []
        self.__right_dead_animations = []
        self.__left_dead_animations = []

        # animation speeds
        # todo fix the animation speed so it gets faster as the players speed increases - use log but more thought is needed

        self.__atacking_animation_speed = int(math.sqrt(self.speed) / 2) if int(math.sqrt(self.speed) / 2) > 1 else 1
        self.__moving_animation_speed = int(math.sqrt(self.speed) / 2) if int(math.sqrt(self.speed) / 2) > 1 else 1
        self.__idle_animation_speed = 1
        self.__dead_animation_speed = 1

        # animation counters - to track which image we should be showing at any time
        self.__attacking_animation_counter = 0
        self.__dead_animation_counter = 0
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
        self.rect.centery = 680

        self.slash = False
#        self.__print_rect()

        # endregion

    # region PUBLIC FUNCTIONS

    def idle(self):
        """
        Default state when player is not doing anything
        :return:
        """
        # forces the player to remain attacking for the full attack duration
        if self.state != "Attacking":
            self.state = "Idle"

            #print(self.__left_dead_animations)

    def move(self, key):
        """
        Handles moving of the player
        :param key: the key pressed by the user
        :return:
        """
        if self.state != "Attacking":
            self.state = "Moving"
            if key == pygame.K_LEFT:
                self.rect.centerx = self.rect.centerx - self.speed
                self.direction = "Left"
            elif key == pygame.K_RIGHT:
                self.rect.centerx = self.rect.centerx + self.speed
                self.direction = "Right"
            else:
                self.state = "Idle"

    def attack(self):
        """
        Called when the user hits the attack button
        :return:
        """
        self.state = "Attacking"

    def finish_attack(self):
        self.slash = True

    def take_damage(self, creep):
        if self.state != "Dead":
            self.current_health = self.current_health - creep.damage
            #print(self.current_health)
            if self.current_health < 0:
                self.state = "Dead"


    def display(self):
        """
        Calls the animate function based on direction/state
        :return: A scaled image and the players height and width
        """
        # animate the player when it's idle
        print("player state {0}".format(self.state))
        if self.state == "Idle":
            if self.direction == "Right":
                return self.__animate(self.__right_idle_animations)
            else:
                return self.__animate(self.__left_idle_animations)
        # animate the player when it's moving
        elif self.state == "Moving":
            if self.direction == "Right":
                return self.__animate(self.__right_moving_animations)
            else:
                return self.__animate(self.__left__moving_animations)
        # animate the player when it's attacking
        elif self.state == "Attacking":
            if self.direction == "Right":
                return self.__animate(self.__right_attacking_animations)
            else:
                return self.__animate(self.__left_attacking_animations)
        elif self.state == "Dead" or self.state == "Dead":
            #print("PLAYER HAS DIED.")
            if self.direction == "Right":
                print(self.__right_dead_animations)
                return self.__animate(self.__right_dead_animations)
            else:
                print(self.__left_dead_animations)
                return self.__animate(self.__left_dead_animations)

    # endregion

    # region PRIVATE FUNCTIONS
    def __animate(self, animations):
        """
        calls the helper classes animate function.
        # todo make this function even more generic as we are checkking animation states in this and the display func
        :param animations: a list of animations to use
        :return: scaled image and the objects rectangle
        """
        if self.state == "Idle":
            # run the generic animate function which returns an image, the current counter so player can keep track
            # and the current animation tick
            self.__idle_animation_counter, self.__animation_tick, image =\
                animate(self.__animation_tick, self.__idle_animation_speed, self.__idle_animation_counter, animations)
            return pygame.transform.scale(image, (self.rect.width, self.rect.height))

        elif self.state == "Moving":
            self.__moving_animation_counter, self.__animation_tick, image =\
                animate(self.__animation_tick, self.__moving_animation_speed, self.__moving_animation_counter, animations)
            return pygame.transform.scale(image, (self.rect.width, self.rect.height))

        elif self.state == "Attacking":
            # less than half way through the full attack animation, do the attack animation normally
            if self.__attacking_animation_counter < len(animations)  / 2:
                self.__attacking_animation_counter, self.__animation_tick, image = \
                    animate(self.__animation_tick, self.__atacking_animation_speed, self.__attacking_animation_counter,
                            animations)
            elif self.__attacking_animation_counter > len(animations)  / 2:
                # in the second half of the animation we want to pause on the first frame
                if not self.slash:
                    self.__attacking_animation_counter, self.__animation_tick, image = \
                        animate(self.__animation_tick, self.__atacking_animation_speed, self.__attacking_animation_counter,
                                animations, pause=True)
                    print("pausing slash = {0}".format(self.slash))
                # user has released the space button so we can finish up our animation
                if self.slash:
                    self.__attacking_animation_counter, self.__animation_tick, image = \
                        animate(self.__animation_tick, self.__atacking_animation_speed, self.__attacking_animation_counter,
                                animations)
                    print("slashing {0}".format(self.slash))
            # complete the entire set of animations.
            if self.__attacking_animation_counter == 0:
                self.slash = False
                self.state = "Idle"
                print("animation complete, setting idddle and not slash {0} player is now {1}".format(self.slash, self.state))
            return pygame.transform.scale(image, (self.rect.width, self.rect.height))


        elif self.state == "Dead":
            print("PLAYER IS NOW DEAD ")
            if self.__dead_animation_counter == len(animations) -1:
                self.__dead_animation_counter, self.__animation_tick, image = \
                    animate(self.__animation_tick, self.__dead_animation_speed, self.__dead_animation_counter,
                            animations, pause=True)
                self.died = True
            else:
                print("ANIMATING A Dead PLAYER")
                self.__dead_animation_counter, self.__animation_tick, image = \
                    animate(self.__animation_tick, self.__dead_animation_speed, self.__dead_animation_counter,
                            animations)
            if self.__dead_animation_counter == 0:
                self.state = "Dead"
            return pygame.transform.scale(image, (self.rect.width, self.rect.height))



    def __load_animations(self):
        """
        Calls the helper function load_animations which fills an animation list
        :return:
        """
        self.__idle_animations_right = load_animations(self.__right_idle_animations, self.__idle_path_right)
        self.__idle_animations_left = load_animations(self.__left_idle_animations, self.__idle_path_left)
        self.__right_moving_animations = load_animations(self.__right_moving_animations, self.__right_moving_path)
        self.__left__moving_animations = load_animations(self.__left__moving_animations, self.__left_moving_path)
        self.__left_attacking_animations = load_animations(self.__left_attacking_animations, self.__left_attacking_path)
        self.__right_attacking_animations = load_animations(self.__right_attacking_animations, self.__right_attacking_path)
        print("loading death animations into {0} from {1}".format(self.__left_dead_animations, self.__left_dead_path))

        self.__left_dead_animations = load_animations(self.__left_dead_animations, self.__left_dead_path)
        self.__right_dead_animations = load_animations(self.__right_dead_animations, self.__right_dead_path)

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





