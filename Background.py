import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Art/Backgrounds/day.png")
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]


