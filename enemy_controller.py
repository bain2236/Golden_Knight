import enemies, random, names



class Enemy_controller():
    """
    Main enemy controller
    Handles:
        Spawning enemy
        Keeping track of enemies alive
    """
    def __init__(self, screen_width, screen_height):
        # a selection of enemy types
        self.enemy_types = ["small_enemy", "big_enemy"]
        self.creeps = []
        self.game_tick = 0
        # it's a controller so he's allowed to know how big things are.
        self.screen_width = screen_width
        self.screen_height = screen_height


    def update(self):
        """
        This function will be called each tick of the game loop
        it will randomly spawn enemies, keep track of enemies, and update enemies
        it will eventually work with a collision detection module
        :return:
        """
        # uses an internal game ticker - incremented everytime the game ticks
        self.game_tick += 1
        # used for debugging
        if self.game_tick % 30 == 0:
            print("enemies in game {0}".format(self.creeps))

        # randomly spawn an enemy between every X and XX calls.
        # the lower the first rand - the more frequent
        # the larger the range the more varied the spawn times will be
        # eg 30, 60 - between 30 and 60 ticks will spawn and enemy if the tick counter has no remainder
        if self.game_tick % random.randint(30, 60) == 0:
            self.__spawn_enemy()
            self.game_tick = 0
        self.__update_enemies()




    def __spawn_enemy(self):
        # creates an enemy by calling the factory with a random name just for fun

        # maybe do something fun with the names, like generate end game cinematic in which it scrolls through
        # gravestones with all the names of the enemies you killed

        self.creeps.append(enemies.build_enemy(random.choice(self.enemy_types), name=names.get_first_name(),
                                               screen_size = [self.screen_width, self.screen_height]))

    def __update_enemies(self):
        # we have creeps, move them
        if self.creeps:
            for creep in self.creeps:
                creep.move()



