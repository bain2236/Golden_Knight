import pygame, sys
from pygame.locals import *
from Player import Player



class Main:



    def __init__(self):
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.HEIGHT = 500
        self.WIDTH = 700
        self.FPS = 60
        self.done = False
        self.screen = None
        self.clock = None
        self.key_press = None



    def setup_game(self):
        # Setup
        pygame.init()
        player = Player()

        # Set the width and height of the screen [width,height]
        size = [self.WIDTH, self.HEIGHT]
        self.screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Platform V1")

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # Hide the mouse cursor
        pygame.mouse.set_visible(0)

        return player

    def draw_object(self, obj):
        self.screen.blit(obj.display(), (obj.position["x"], obj.position["y"]))

    def event_handler(self, player):
        # determin if X was clicked, or Ctrl+W or Alt+F4 was used
        if self.key_press is None:
            player.idle()
        for event in pygame.event.get():
            #print ("EVENT")
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.key_press = event.key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.key_press = None
                    player.idle()
        if self.key_press == K_ESCAPE:
            self.done = True
        if self.key_press is not None:
            player.move(self.key_press)

    def start_game(self, player):
        # -------- Main Program Loop -----------
        while not self.done:
            self.screen.fill(self.WHITE)

            self.event_handler(player)

            # draw the player.
            self.draw_object(player)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()


            # Limit frames per second
            self.clock.tick(self.FPS)

    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    game_controller = Main()
    player = game_controller.setup_game()
    game_controller.start_game(player)
