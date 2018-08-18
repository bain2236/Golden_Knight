import pygame, sys
from pygame.locals import *
from player import Player
from sounds import Sound
from background import Background
from enemy_controller import Enemy_controller
from collision_controller import Collision_controller
from user_interface_controller import User_interface



class Game:
    """
    Main game controller
    """
    def __init__(self, player, screen, clock):
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.HEIGHT = 900
        self.WIDTH = 1920
        self.FPS = 30
        self.game_over = False
        self.screen = screen
        self.clock = clock
        self.key_press = None
        self.background = Background()
        self.sound = Sound()
        self.enemy_controller = Enemy_controller(self.WIDTH, self.HEIGHT)
        self.collision_controller = Collision_controller()
        self.player = player


    def draw_object(self, obj):
        """
        draws whatever object is passed in
        :param obj:
        :return:
        """
        if isinstance(obj, Player) and not obj.died:
            #print("drawing the player")
            self.screen.blit(obj.display(), obj.rect)
        elif isinstance(obj, Player):
            #print("drawing teh dead player")
            self.screen.blit(obj.display(), obj.rect)

        elif not obj.died:
           # print("drawing not dead object {0}".format(obj))
            self.screen.blit(obj.display(), obj.rect)



    def event_handler(self, player):
        """
        Handles button pushes by the user
        :param player:
        :return:
        """
        if self.key_press is None:
            # nothing pressed - player is idle
            player.idle()
        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.game_over = True
            # handle which button has been pressed
            elif event.type == pygame.KEYDOWN:
                self.key_press = event.key
            # allows the player to keep a button pressed to continously handle that event
            # by setting the key press to none if the key is released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.key_press = None
                    if player.state != "Dead":
                        player.idle()
                if event.key == pygame.K_SPACE:
                    player.finish_attack()
                    self.key_press = None

        if player.state != "Dead":
            # move the player with whatever direction was used.
            if self.key_press is not None and not self.key_press == pygame.K_SPACE:
                player.move(self.key_press)
            # attack button pressed
            if self.key_press == pygame.K_SPACE:
                player.attack()
        # handles escape being pushed to quit the game
        if self.key_press == K_ESCAPE:
            self.game_over = True




    def play_game(self):
        """
        Main game loop
        :param player:
        :return:
        """
        # turn on background music
        self.sound.play_music()
        # fill the screen white
#        self.screen.fill(self.WHITE)
        # initial draw of all background layers
        sky, ground, near, far, rect = self.background.draw_all((self.WIDTH, self.HEIGHT))
        # blit all elements to the screen
        self.screen.blit(sky, rect)
        self.screen.blit(far, rect)
        self.screen.blit(near, rect)
        self.screen.blit(ground, rect)

        # used to debug the draw layers function
        #self.screen.fill(self.WHITE)
        while not self.player.died:
            # handles button pushes
            self.event_handler(self.player)

            # update enemy positions and spawn new enemies
            self.enemy_controller.update()

            # DO ALL THE DRAWING

            # draws just the ground layers - stops game asset ghosting
            pos, box = self.background.draw_ground_layers(self.HEIGHT, self.WIDTH)
            self.screen.blit(sky, pos, box)
            self.screen.blit(far, pos, box)
            self.screen.blit(near, pos, box)
            self.screen.blit(ground, pos, box)

            # draw any creeps that the enemy_controller has
            for creep in self.enemy_controller.creeps:
                # check if t heres any collisions
                self.collision_controller.is_collided_with(self.player, creep)
                self.draw_object(creep)

            # draw the player.
            self.draw_object(self.player)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit frames per second
            self.clock.tick(self.FPS)
            # print(self.clock.get_fps())


if __name__ == "__main__":
    # Setup
    pygame.init()
    # Set the width and height of the screen [width,height]

    HEIGHT = 900
    WIDTH = 1920
    size = [WIDTH, HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Golden Knight V0.1")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    hud = User_interface(WIDTH, HEIGHT, screen, clock)

    # Hide the mouse cursor
#    pygame.mouse.set_visible(0)
    playing = False
    user_quit = False
    # user still wants to play
    while not user_quit:

        # show the main menu until the player selects play
        user_quit = hud.main_menu()
        # create a game and start playing - return from playing if you die
        player = Player(WIDTH, HEIGHT)
        game_controller = Game(player, screen, clock)
        game_controller.play_game()

        # user has died. sit in this loop until they decide to restart or now
        # sit inside the game over screen until the user hits restart or not
        restart = hud.game_over()
        if restart:
            user_quit = False
        else:
            user_quit = True

