import pygame
import math
import os
import time
from setting import PATH
from color_setting import *

water_anim = []
for i in range(6):
    water_anim.append(pygame.transform.scale(pygame.image.load(os.path.join('image_2/Enemy/', f'fireA-{i}.png')), (60, 70)))


class Enemy:
    def __init__(self, max_hp):
        self.width = 60
        self.height = 60
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.money = 0

        self.path = PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.x = self.path[0][0]
        self.y = self.path[0][1]

        self.image = None
        self.animation = []
        self.animation_index = 0
        self.last_update = time.time()
        self.frame_rate = 1


    def update(self):
        """
        Move enemy
        :return: None
        """
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        max_count = int(distance / self.stride)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride
        delta_y = unit_vector_y * self.stride

        # update the position and counter
        if self.move_count <= max_count:
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.x, self.y = self.path[self.path_index]

        # update the animation count
        now = time.time()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.animation_index += 1
            if self.animation_index < len(self.animation)-1:
                self.image = self.animation[self.animation_index]
            else:
                self.image = self.animation[self.animation_index]
                self.animation_index = 0

    def draw_health_bar(self, surf):
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """
        hp_width = self.width * (self.hp / self.max_hp)
        pygame.draw.rect(surf, RED_1, [self.x - self.width // 2, self.y - self.height // 2 - 5, self.width, 6], 0)
        pygame.draw.rect(surf, RED_2, [self.x - self.width // 2, self.y - self.height // 2 - 5, hp_width, 6], 0)

    def draw(self, surf):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.image = self.animation[self.animation_index]
        surf.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        self.draw_health_bar(surf)



class Water(Enemy):
    def __init__(self, max_hp):
        super().__init__(max_hp)
        self.money = 20
        self.animation = water_anim[:]



