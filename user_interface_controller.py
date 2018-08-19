import pygame, os, functions


class User_interface():
    def __init__(self, width, height, __screen, __clock):
        self.__screen_width = width
        self.__screen_height = height
        self.__screen = __screen
        self.__clock = __clock

        self.__restart_button_path = "UI/Buttons/restart.png"
        self.__quit_button_path = "UI/Buttons/quit.png"
        self.__play_button_path = "UI/Buttons/play.png"
        self.__leaderboard_button_path = "UI/Buttons/leaderboard.png"
        self.__main_logo_path = "UI/Buttons/main_logo.png"
        self.__game_over_path = "UI/Buttons/game_over.png"
        self.__menu_background_path = "UI/menu.png"
        self.__restart_button = Button(self.__restart_button_path)
        self.__quit_button = Button(self.__quit_button_path)
        self.__play_button = Button(self.__play_button_path)
        self.__leaderboard_button = Button(self.__leaderboard_button_path)
        self.__main_logo_button = Button(self.__main_logo_path)
        self.__game_over_button = Button(self.__game_over_path)
        self.__menu_background = pygame.transform.scale(functions.load_art(self.__menu_background_path),
                                                        (self.__screen_width, self.__screen_height))


    def game_over(self):
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # left mouse button pressed
                    pos = pygame.mouse.get_pos()
                    if self.__quit_button.rect.collidepoint(pos):
                        pygame.quit()
                        quit()
                    if self.__restart_button.rect.collidepoint(pos):
                        print("PLAY AGAIN")
                        return True

            self.__screen.blit(self.__game_over_button.image, self.__button_position(self.__game_over_button, 1))
            self.__screen.blit(self.__restart_button.image, self.__button_position(self.__restart_button, 3))
            self.__screen.blit(self.__quit_button.image, self.__button_position(self.__quit_button, 4))

            pygame.display.update()
            self.__clock.tick(100)


    def main_menu(self):
        print("showing main menu")
        self.__screen.blit(self.__menu_background, (0,0))

        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # left mouse button pressed
                    pos = pygame.mouse.get_pos()
                    if self.__quit_button.rect.collidepoint(pos):
                        pygame.quit()
                        quit()
                    if self.__main_logo_button.rect.collidepoint(pos):
                        print("this is an easter egg")
                    if self.__play_button.rect.collidepoint(pos):
                        print("lets create a game to play")
                        return

            self.__screen.blit(self.__main_logo_button.image, self.__button_position(self.__main_logo_button, 1))
            self.__screen.blit(self.__play_button.image, self.__button_position(self.__play_button, 2))
            self.__screen.blit(self.__leaderboard_button.image, self.__button_position(self.__leaderboard_button, 3))
            self.__screen.blit(self.__quit_button.image, self.__button_position(self.__quit_button, 4))

            pygame.display.update()
            self.__clock.tick(100)


    def __button_position(self, button, position):
        button.rect.center = (self.__centre_button(button), self.__evenly_height(button, position))
        return button.rect.center

    def __centre_button(self, button):
        return (self.__screen_width / 2) - (button.rect.width / 2)

    def __evenly_height(self, button, position, expected_number=4):
        # expected number is the amount of things we expect to be evenly heighting
        return (self.__screen_height / expected_number * position) - button.rect.height


class Button(pygame.sprite.Sprite):
    def __init__(self, button_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = functions.load_art(button_path)
        self.rect = self.image.get_rect()





