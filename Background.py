import pygame, os, random


class Background(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.__path_to_backgrounds = "C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Art/Backgrounds/"
        self.__path_to_sky = "sky/"
        self.__path_to_ground = "ground/"
        self.__path_to_near = "near/"
        self.__path_to_far = "far/"
        self.__possible_sky = []
        self.__possible_ground = []
        self.__possible_far = []
        self.__possible_near = []


        self.__image = self.load_background()
#        self.__image_scaled = pygame.transform.scale(self.__image, screen_size)
        self.__rect = self.__image.get_rect()
        #self.__rect.left, self.rect.top = [0, 0]

    def load_background(self):
        sky = self.__load_layer(self.__path_to_backgrounds, self.__path_to_sky, self.__possible_sky)
        ground = self.__load_layer(self.__path_to_backgrounds, self.__path_to_ground, self.__possible_ground)
        near = self.__load_layer(self.__path_to_backgrounds, self.__path_to_near, self.__possible_far)
        far = self.__load_layer(self.__path_to_backgrounds, self.__path_to_far, self.__possible_near)


    def __load_layer(self, path, layer_dir, possible_layers):
        path_to_layer = path + layer_dir
        images = None
        # load right idle animations
        for _, _, images in os.walk(path_to_layer):
            pass
        if images is not None:
            for image in images:
                if ".png" in image:
                    image = pygame.image.load(os.path.join((path_to_layer + image)))
                    self.__possible_backgrounds.append(image)
        return random.choice(self.__possible_backgrounds)


    def draw_layer(self, layer, screen_size):
        return pygame.transform.scale(layer, screen_size), self.__rect





    def draw_background(self):
        return self.__image_scaled, self.__rect