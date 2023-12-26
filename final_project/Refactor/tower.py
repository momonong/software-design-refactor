from attack_strategy import AOE, SingleAttack, Snipe
import os
import pygame

fireman_image = [pygame.transform.scale(pygame.image.load(f"image/Tower/Fireman/fireman-{i}.png"), (int(466//3.5), int(260//3.5))) for i in range(6)]
firetruck_image = [pygame.transform.scale(pygame.image.load(f"image/Tower/FireTruck/firetruck-{i}.png"), (int(513/3), int(220/3))) for i in range(6)]
extinguisher_image = [pygame.transform.scale(pygame.image.load(f"image/Tower/FireExtinguisher/fireextinguisher-{i}.png"), (int(360/3), int(260/3))) for i in range(6)]

plot_image = pygame.transform.scale(pygame.image.load(os.path.join("image/Tower", "vacant_plot.png")), (40, 40))


class Vacancy:
    def __init__(self, x, y):
        self.image = plot_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int) -> bool:
        """
        :param x: mouse pos x
        :param y: mouse pos y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False


# tower (product)
class Tower:
    """ parent class of towers """
    def __init__(self, x: int, y: int, attack_strategy, image):
        self.image = image[0]  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.level = {'damage' : 0,
                      'range' : 0,
                      'cd_time' : 0}  # level of the tower
        self._damage = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]  # tower damage
        self._range = [100, 110, 120, 130, 140, 150]  # tower attack range
        self.cd_count = 0  # used in self.is_cool_down()
        self._cd_max_count = [60, 50, 40, 30, 20, 10]  # used in self.is_cool_down()
        self.upgrade_cost = [100, 150, 200, 250, 300, 350]
        self.sell_cost = [300, 600, 900, 1200, 1500, 1800]
        self.build_cost = 200

        self.animation = image
        self._anim_time = [(i/len(self.animation)-0.01) for i in self._cd_max_count]
        self.animation_index = 0
        self.last_anim = pygame.time.get_ticks()
        self.is_update_anim = False

        self.attack_strategy = attack_strategy  # chose an attack strategy (AOE, single attack ....)

    @classmethod
    def Fireman(cls, x, y):
        fireman = cls(x, y, SingleAttack(), fireman_image)
        fireman._damage = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0]
        fireman._range = [130, 140, 150, 160, 170, 180]
        fireman._cd_max_count = [100, 85, 70, 55, 40, 30]
        fireman._anim_time = [(i / len(fireman.animation)+(i)) for i in fireman._cd_max_count]
        return fireman

    @classmethod
    def Firetruck(cls, x, y):
        firetruck = cls(x, y, AOE(), firetruck_image)
        firetruck._damage = [1.2, 1.4, 1.6, 1.8, 2.0, 2.2]
        firetruck._range = [130, 140, 150, 160, 170, 180]
        firetruck._cd_max_count = [110, 100, 80, 70, 60, 50]
        firetruck._anim_time = [(i / len(firetruck.animation)+(i)) for i in firetruck._cd_max_count]
        return firetruck

    @classmethod
    def Extinguisher(cls, x, y):
        extinguisher = cls(x, y, Snipe(), extinguisher_image)
        extinguisher._range = [100, 105, 110, 115, 120, 125]  # tower attack range
        extinguisher._cd_max_count = [150, 130, 110, 90, 70, 50]
        extinguisher._anim_time = [(i / len(extinguisher.animation)+(i)) for i in extinguisher._cd_max_count]
        return extinguisher

    def attack(self, enemy_group):
        # cd
        if self.cd_count < self._cd_max_count[self.level['cd_time']]:
            self.cd_count += 1
            return
        # syntax: attack_strategy().attack(tower, enemy_group, cd_count)
        # It's something like you hire a "Strategist" to decide how to attack the enemy
        # You can add other ways of attack just by expanding the "attack_strategy.py"
        self.cd_count = self.attack_strategy.attack(enemy_group, self, self.cd_count)

    def attack_anim(self):
        now = pygame.time.get_ticks()
        if self.is_update_anim == True:
            if now - self.last_anim >= self._anim_time[self.level['cd_time']]:
                self.last_anim = now
                self.animation_index += 1
                if self.animation_index < len(self.animation) - 1:
                    self.image = self.animation[self.animation_index]
                else:
                    self.image = self.animation[self.animation_index]
                    self.animation_index = 0
                    self.is_update_anim = False


    def get_upgrade_cost(self, upgrade_name:str):
        if upgrade_name == 'damage':
            return self.upgrade_cost[self.level['damage']]
        if upgrade_name == 'range':
            return self.upgrade_cost[self.level['range']]
        if upgrade_name == 'cd_time':
            return self.upgrade_cost[self.level['cd_time']]

    def get_sell_cost(self):
        return self.sell_cost[int((self.level['damage']+
                                      self.level['range']+
                                      self.level['cd_time'])/3)]

    @property
    def range(self):
        return self._range[self.level['range']]

    @property
    def damage(self):
        return self._damage[self.level['damage']]

    def clicked(self, x, y):
        return True if self.rect.collidepoint(x, y) else False
