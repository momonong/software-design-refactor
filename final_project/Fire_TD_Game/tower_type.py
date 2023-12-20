import pygame
from tower import Tower
import time

FPS = 60
sandbag_images = [pygame.transform.scale(pygame.image.load(f"image_2/Tower/Fireman/fireman-{i}.png"), (int(466//3.5), int(260//3.5))) for i in range(6)]
wiper_images = [pygame.transform.scale(pygame.image.load(f"image_2/Tower/FireTruck/firetruck-{i}.png"), (int(513/3), int(220/3))) for i in range(6)]
pump_images = [pygame.transform.scale(pygame.image.load(f"image_2/Tower/FireExtinguisher/fireextinguisher-{i}.png"), (int(360/3), int(260/3))) for i in range(6)]

sandbag_anim = [pygame.transform.scale(pygame.image.load(f"image_2/Tower/Fireman/fireman-{i}.png"), (int(466//3.5), int(260//3.5))) for i in range(6)]
wiper_anim = [pygame.transform.scale(pygame.image.load(f"image_2/Tower/FireTruck/firetruck-{i}.png"), (int(513/3), int(220/3))) for i in range(6)]
pump_anim = [pygame.transform.scale(pygame.image.load(f"image_2/Tower/FireExtinguisher/fireextinguisher-{i}.png"), (int(360/3), int(260/3))) for i in range(6)]

sandbag_bullets = [pygame.transform.scale(pygame.image.load(f"image/tower/sandbag/bullet/sabow-{i}.png"), (int(200/4), int(200/4))) for i in range(6)]

class Sandbag(Tower):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        #  tower geometry
        self.images = sandbag_images
        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()
        self.market_price = 100
        # level: 0~2
        self.level = {
            "range": 0,
            "damage": 0,
            "cool down": 0,
        }
        # ability: level 0~2
        self.ability = {
            "range": [90, 110, 130],
            "damage": [4.0, 7.5, 10.0],
            "cool down": [1.5, 1.0, 0.8]
        }
        # price
        self.upgrade_market_price = {
            "range": [0, 100, 130],
            "damage": [0, 80, 120],
            "cool down": [0, 80, 100]}

        self.animation = sandbag_anim
        self.frame_rate = [i / len(self.animation) for i in self.ability['cool down']]

        self.bullet_anim = sandbag_bullets

class Wiper(Tower):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        #  tower geometry
        self.images = wiper_images
        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()
        self.market_price = 150
        # level: 0~2
        self.level = {
            "range": 0,
            "damage": 0,
            "cool down": 0,
        }
        # ability: level 0~2
        self.ability = {
            "range": [100, 120, 180],
            "damage": [1.0, 1.5, 2.5],
            "cool down": [2.0, 1.8, 1.4]
        }
        # price
        self.upgrade_market_price = {
            "range": [0, 120, 140],
            "damage": [0, 100, 120],
            "cool down": [0, 120, 150],
        }

        self.animation = wiper_anim
        self.frame_rate = [i / len(self.animation) for i in self.ability['cool down']]

    def attack(self, enemies):
        """
        AOE attack
        :param enemies: list
        :return: None
        """
        if self.is_cooling_down and self.update_anim == False:
            for en in enemies:
                if self.enemy_in_range(en):
                    self.update_anim = True
                    en.hp -= self.ability["damage"][self.level["damage"]]
                  # AOE attack




class Pump(Tower):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        #  tower geometry
        self.images = pump_images
        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()
        self.market_price = 150
        # level: 0~2
        self.level = {
            "range": 0,
            "damage": 0,
            "cool down": 0,
        }
        # ability: level 0~2
        self.ability = {
            "range": [100, 120, 140],
            "damage": [1.5, 2.0, 3.0],
            "cool down": [0.4, 0.25, 0.1]
        }
        # price
        self.upgrade_market_price = {
            "range": [0, 100, 120],
            "damage": [0, 80, 120],
            "cool down": [0, 80, 100],
        }

        self.animation = pump_anim
        self.frame_rate = [i / len(self.animation) for i in self.ability['cool down']]



