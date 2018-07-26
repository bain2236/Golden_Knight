import pygame, sys
from pygame.locals import *
from player import Player
from sounds import Sound
from background import Background


class Main:



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
        self.background = None
        self.sound = None



    def setup_game(self):
        # Setup
        pygame.init()
        player = Player(self.WIDTH, self.HEIGHT)
        self.background = Background((self.WIDTH, self.HEIGHT))
        self.sound = Sound()



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
#        print("draw_object return {0}".format(self.screen.blit(obj.display(), obj.rect)))
        self.screen.blit(obj.display(), obj.rect)

    def event_handler(self, player):
        # determine if X was clicked, or Ctrl+W or Alt+F4 was used
        if self.key_press is None:
            print("nothing pressed, player is idle")
            player.idle()
        for event in pygame.event.get():
            #print ("EVENT")
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.key_press = event.key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                    print("space released")
                    self.key_press = None
                    player.idle()
        if self.key_press == K_ESCAPE:
            self.done = True
        if self.key_press is not None and not self.key_press == pygame.K_SPACE:
            player.move(self.key_press)
        if self.key_press == pygame.K_SPACE:
            print("space pushed")
            player.attack()



    def start_game(self, player):
        # -------- Main Program Loop -----------
        self.sound.play_music()
        self.screen.fill([255, 255, 255])
        sky, ground, near, far, rect = self.background.draw_all((self.WIDTH, self.HEIGHT))
#        print("background draw all return{0}".format(self.background.draw_all((self.WIDTH, self.HEIGHT))))
        self.screen.blit(sky, rect)
        self.screen.blit(far, rect)
        self.screen.blit(near, rect)
        self.screen.blit(ground, rect)




        #self.sound.play_music()
        while not self.done:
            pos, box = self.background.draw_layer_around_obj(player)



            self.screen.blit(sky, pos, box)
            self.screen.blit(far, pos, box)
            self.screen.blit(near, pos, box)
            self.screen.blit(ground, pos, box)




            self.event_handler(player)

            # draw the player.
            self.draw_object(player)

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
