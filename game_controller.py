import pygame, sys
from pygame.locals import *
from player import Player
from sounds import Sound
from background import Background
from enemy_controller import Enemy_controller



class Main:
    """
    Main game controller
    """
    def __init__(self):
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.HEIGHT = 900
        self.WIDTH = 1920
        self.FPS = 30
        self.done = False
        self.screen = None
        self.clock = None
        self.key_press = None
        self.background = Background()
        self.sound = Sound()
        self.enemy_controller = Enemy_controller(self.WIDTH, self.HEIGHT)



    def setup_game(self):
        """
        initial pygame setup, screen, clock and player
        :return: Player object
        """
        # Setup
        pygame.init()
        # create player
        player = Player(self.WIDTH, self.HEIGHT)

        # Set the width and height of the screen [width,height]
        size = [self.WIDTH, self.HEIGHT]
        self.screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Golden Knight V0.1")

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # Hide the mouse cursor
        pygame.mouse.set_visible(0)

        return player

    def draw_object(self, obj):
        """
        draws whatever object is passed in
        :param obj:
        :return:
        """
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
                self.done = True
            # handle which button has been pressed
            elif event.type == pygame.KEYDOWN:
                self.key_press = event.key
            # allows the player to keep a button pressed to continously handle that event
            # by setting the key press to none if the key is released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                    self.key_press = None
                    player.idle()
        # handles escape being pushed to quit the game
        if self.key_press == K_ESCAPE:
            self.done = True
        # move the player with whatever direction was used.
        if self.key_press is not None and not self.key_press == pygame.K_SPACE:
            player.move(self.key_press)
        # attack button pressed
        if self.key_press == pygame.K_SPACE:
            player.attack()



    def start_game(self, player):
        """
        Main game loop
        :param player:
        :return:
        """
        # turn on background music
        self.sound.play_music()
        # fill the screen white
        self.screen.fill(self.WHITE)
        # initial draw of all background layers
        sky, ground, near, far, rect = self.background.draw_all((self.WIDTH, self.HEIGHT))
        # blit all elements to the screen
        self.screen.blit(sky, rect)
        self.screen.blit(far, rect)
        self.screen.blit(near, rect)
        self.screen.blit(ground, rect)

        while not self.done:
            # draws just the ground layers - stops game asset ghosting
            pos, box = self.background.draw_ground_layers(self.HEIGHT, self.WIDTH)
            self.screen.blit(sky, pos, box)
            self.screen.blit(far, pos, box)
            self.screen.blit(near, pos, box)
            self.screen.blit(ground, pos, box)

            # draw any creeps that the enemy_controller has
            for creep in self.enemy_controller.creeps:
                self.draw_object(creep)

            # handles button pushes
            self.event_handler(player)

            # draw the player.
            self.draw_object(player)

            # update enemy positions and spawn new enemies
            self.enemy_controller.update()

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit frames per second
            self.clock.tick(self.FPS)
            # print(self.clock.get_fps())

    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    game_controller = Main()
    player = game_controller.setup_game()
    game_controller.start_game(player)
