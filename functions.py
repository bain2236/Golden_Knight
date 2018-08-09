import os, pygame
art_asset_path = ("C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Art/")


"""
Helper functions for use by many classes
"""

def load_animations(animations, animation_path):

    images = None
    # load right idle animations
    for _, _, images in os.walk(art_asset_path + animation_path):
        pass
    #print("images found in {0}{1}".format(art_asset_path, animation_path))
    if images is not None:
        for image in images:
            if image.lower().endswith("png"):
                #print("loading image {0}".format(image))
                image = pygame.image.load(os.path.join((art_asset_path + animation_path + image)))
                animations.append(image)
    return animations



def animate(animation_tick, animation_speed, animation_counter, animations):

    # increment the tick so animations happen at certain points - this the same as the game tick
    animation_tick += 1
    # change the image to the next in the list
    if animation_tick % animation_speed == 0:
        animation_counter += 1
        # animation list has finished, reset it so it starts again.
        if animation_counter > len(animations) - 1:
            animation_counter = 0
            animation_tick = 0
    return animation_counter, animation_tick, animations[animation_counter]

