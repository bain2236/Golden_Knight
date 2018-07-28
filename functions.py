import os, pygame
art_asset_path = ("C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Art/")


def load_animations(animations, animation_path):

    images = None
    # load right idle animations
    for _, _, images in os.walk(art_asset_path + animation_path):
        pass
    if images is not None:
        for image in images:
            if ".png" in image:
                image = pygame.image.load(os.path.join((art_asset_path + animation_path + image)))
                animations.append(image)
    return animations