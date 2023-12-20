import pygame
import time

from enemy import Water



class EnemyGenerator:
    def __init__(self):
        self.enemy_nums = [10, 20, 30, 40, 50]
        self.enemy_hp = [8, 10, 12, 14, 16]
        self.gen_enemy_time = time.time()
        self.period = [0.5, 0.5, 0.3, 0.3, 0.2]

    def generate(self, enemies, wave):
        """
        generate the enemy to the enemy list according to the given wave
        :param enemies: list
        :param wave: int
        :return: None
        """
        if time.time() - self.gen_enemy_time >= self.period[wave] and self.enemy_nums[wave] > 0:  # wave interval
            self.gen_enemy_time = time.time()
            self.enemy_nums[wave] -= 1
            enemies.append(Water(self.enemy_hp[wave]))