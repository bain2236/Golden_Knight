import pygame, sys

class Collision_controller():
    def __init__(self):
        pass

    def is_collided_with(self, player, creep):
        # both objects facing the same direction, which means collision occured in the back

        if player.rect.colliderect(creep.rect) and player.state == "Attacking" and player.direction != creep.direction:
            # player is attacking and facing the enemy
            # damage the enemy
            creep.take_damage(player)
            print("you killed {0}".format(creep.name))
        elif player.rect.colliderect(creep.rect) and player.state == "Attacking" and player.direction == creep.direction:
            # player is attacking but facing the same direction
            player.take_damage(creep)
            print("you were facing the wrong direction")
        elif player.rect.colliderect(creep.rect) and player.state != "Attacking":
            # player was not even atacking. stupid player
            player.take_damage(creep)
            print("you did not attack you have taken {0}".format(creep.damage))


