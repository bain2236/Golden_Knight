import pygame, os, random


class Background(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.__path_to_backgrounds = "C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Art/Backgrounds/"

        self.__possible_backgrounds = []
        self.__image = self.load_background()
        self.__image_scaled = pygame.transform.scale(self.__image, screen_size)
        self.__rect = self.__image.get_rect()
        #self.__rect.left, self.rect.top = [0, 0]

    def load_background(self):
        images = None
        # load right idle animations
        for _, _, images in os.walk(self.__path_to_backgrounds):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    image = pygame.image.load(os.path.join((self.__path_to_backgrounds + image)))
                    self.__possible_backgrounds.append(image)
        return random.choice(self.__possible_backgrounds)


    def draw_background(self):
        return self.__image_scaled, self.__rect