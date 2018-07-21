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


        self.__load_background()



    def __load_background(self):
        self.sky = self.__load_layer(self.__path_to_backgrounds, self.__path_to_sky, self.__possible_sky)
        self.ground = self.__load_layer(self.__path_to_backgrounds, self.__path_to_ground, self.__possible_ground)
        self.near = self.__load_layer(self.__path_to_backgrounds, self.__path_to_near, self.__possible_near)
        self.far = self.__load_layer(self.__path_to_backgrounds, self.__path_to_far, self.__possible_far)
        self.__rect = self.sky.get_rect()


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
                    possible_layers.append(image)
        return random.choice(possible_layers)


    def draw_layer(self, layer, screen_size):
        return pygame.transform.scale(layer, screen_size), self.__rect


    def draw_all(self, screen_size):
        sky, _ = self.draw_layer(self.sky, screen_size)
        ground, _ = self.draw_layer(self.ground, screen_size)
        near, _ = self.draw_layer(self.near, screen_size)
        far, _ = self.draw_layer(self.far, screen_size)
        return sky, ground, near, far, self.__rect


    def draw_layer_around_obj(self, obj):
        return (obj.rect.x, obj.rect.y),\
               (obj.rect.x, obj.rect.y, obj.rect.height + obj.rect.height / 2, obj.rect.width + obj.rect.width / 2)


    def draw_background(self):
        return self.__image_scaled, self.__rect