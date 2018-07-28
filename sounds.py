import pygame, os


class Sound:
    """
    sound controller for the main game.
    """
    def __init__(self):
        pygame.mixer.init()
        self.background_music = []

        self.__asset_path = "C:/Users/Alex_/PycharmProjects/py_side_scroller/Assets/Sound"
        self.__background_music_path = "/Music/"
        self.__load_songs()



    def __load_songs(self):
        background_music = None
        # load idle animations
        for _, _, background_music in os.walk(self.__asset_path + self.__background_music_path):
            pass
        # grabs all music from the folder and loads it
        if background_music is not None:
            for song in background_music:
                if ".mp3" in song:
                    song = (os.path.join((self.__asset_path + self.__background_music_path + song)))
                    pygame.mixer.music.load(song)
                    self.background_music.append(song)

    def play_music(self):
        # adds all songs to a queue
        for song in self.background_music:
            pygame.mixer.music.queue(song)
        pygame.mixer.music.play()