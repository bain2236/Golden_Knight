import enemies, random, names



class Enemy_controller():
    def __init__(self, screen_width, screen_height):
        self.enemy_types = ["small_enemy"]
        self.creeps = []
        self.game_tick = 0
        self.screen_width = screen_width
        self.screen_height = screen_height


    def update(self):
        """
        This function will be called each tick of the game loop
        it will randomly spawn enemies, keep track of enemies, and update enemies
        it will eventually work with a collision detection module
        :return:
        """
        self.game_tick += 1
        if self.game_tick % 30 == 0:
            print("enemies in game {0}".format(self.creeps))

        # randomly spawn an enemy between every X and XX calls.
        if self.game_tick % random.randint(30, 60) == 0:
            self.__spawn_enemy()
            self.game_tick = 0
        self.__update_enemies()




    def __spawn_enemy(self):

        self.creeps.append(enemies.build_enemy(random.choice(self.enemy_types), name=names.get_first_name(),
                                               screen_size = [self.screen_width, self.screen_height]))

    def __update_enemies(self):
        # we have creeps, move them
        if self.creeps:
            for creep in self.creeps:
                creep.move()



