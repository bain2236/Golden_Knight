import pygame, os


class Sound:
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
        if background_music is not None:
            for song in background_music:
                if ".mp3" in song:
                    song = (os.path.join((self.__asset_path + self.__background_music_path + song)))
                    pygame.mixer.music.load(song)
                    self.background_music.append(song)


    # def play_music(self):
    #
    #     pygame.mixer.music.play(-1, 0.0)

    def play_music(self):
        for song in self.background_music:
            pygame.mixer.music.queue(song)
        pygame.mixer.music.play()