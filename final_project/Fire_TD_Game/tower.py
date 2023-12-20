import pygame
import time
import math

FPS = 60
btn_image = {
    "selling": pygame.transform.scale(pygame.image.load("image/tower/sell.png"), (45, 45)),
    "range": pygame.transform.scale(pygame.image.load("image/tower/range.png"), (30, 30)),
    "damage": pygame.transform.scale(pygame.image.load("image/tower/damage.png"), (20, 30)),
    "cool down": pygame.transform.scale(pygame.image.load("image/tower/cool_down.png"), (30, 30)),
}
menu_image = pygame.transform.scale(pygame.image.load("image/tower/upgrade_menu.png"), (200, 200))

class Tower:
    def __init__(self, x, y, name):
        #  tower geometry
        self.x = x
        self.y = y
        self.images = [None, None, None]
        self.width = 0
        self.height = 0
        self.market_price = 0
        self.name = name
        # level: 0~2
        self.level = {
            "range": 0,
            "damage": 0,
            "cool down": 0,
        }
        # ability: level 0~2
        self.cooling_timer = time.time() - 1
        self.ability = {
            "range": [0, 0, 0],
            "damage": [0, 0, 0],
            "cool down": [0, 0, 0],
        }
        # price
        self.upgrade_market_price = {
            "range": [0, 0, 0],
            "damage": [0, 0, 0],
            "cool down": [0, 0, 0],
        }
        # others
        self.menu = None
        self.update_flip = False

        self.animation = []
        self.animation_index = 0
        self.last_update = time.time()
        self.frame_rate = [0, 0, 0]
        self.update_anim = False

        self.bullet = None
        self.bullet_anim = []
        self.bullet_animation_index = 0
        self.bullet_last_update = time.time()
        self.bullet_frame_rate = 3
        self.update_bullet_anim = False



    def upgrade(self, x, y, tech_level, money):
        """
        if the button is clicked, upgrade the corresponding ability and return the cost
        :param x: int
        :param y: int
        :param tech_level: int
        :param money: int
        :return: int, str
        """
        notice = None
        if self.menu:
            option = self.menu.get_items(x, y)
            if option and option != "selling":
                if self.level[option] >= tech_level:
                    notice = f"You need to raise your technology level to upgrade tower {option}"
                elif money < self.upgrade_market_price[option][self.level[option]+1]:
                    notice = f"{self.upgrade_market_price[option][self.level[option] + 1]} is needed for upgrade tower {option}"
                else:
                    money -= self.upgrade_market_price[option][self.level[option]+1]
                    notice = f"Pay {self.upgrade_market_price[option][self.level[option] + 1]} to upgrade tower {option}"
                    self.level[option] += 1
        return money, notice

    def sells(self, x, y, money):
        """
        if "selling" button is clicked, return the selling price and the status
        :param x: int
        :param y: int
        :param money: int
        :return: (int, Bool, str)
        """
        notice = None
        if self.menu:
            option = self.menu.get_items(x, y)
            if option == "selling":
                selling_price = self.market_price
                for name, price in self.upgrade_market_price.items():
                    selling_price += price[self.level[name]]
                money += int(selling_price*0.9)
                notice = f"Recovery {int(selling_price)} from the tower"
        return money, notice

    def call_menu(self, x, y):
        """
        if the tower is selected, call the upgrade menu
        :param x: int
        :param y: int
        :return: None
        """
        if self.is_clicked(x, y):
            self.menu = UpgradeMenu(self.x-5, self.y-10)
        else:
            self.menu = None

    def attack(self, enemies):
        """
        detect the enemies in range and drop their health
        :param enemies: list
        :return: None
        """
        if self.is_cooling_down and self.update_anim == False:
            for en in enemies:
                if self.enemy_in_range(en):
                    self.update_anim = True
                    en.hp -= self.ability["damage"][self.level["damage"]]
                    break  # single attack

    def enemy_in_range(self, enemy):
        """
        return whether the enemy is in the range
        :param enemy: obj
        :return: Bool
        """
        x = enemy.x
        y = enemy.y
        distance = math.sqrt((x-self.x)**2 + (y-self.y)**2)
        if distance <= self.ability["range"][self.level["range"]]:
            return True
        return False

    def is_cooling_down(self):
        """
        return whether the tower is cooling down
        :return: Bool
        """
        cd_time = self.ability["cool down"][self.level["cool down"]]
        if time.time() - self.cooling_timer >= cd_time:
            self.cooling_timer = time.time()
            return True
        return False

    def is_clicked(self, x, y):
        """
        return whether the tower get clicked
        :param x: int
        :param y: int
        :return: Bool
        """
        if (self.x - self.width // 2) < x < (self.x + self.width // 2) \
                and (self.y - self.height // 2) < y < (self.y + self.height // 2):
            return True
        if self.menu and self.menu.is_clicked(x, y):
            return True
        return False


    # def attack_bullet(self):
    #     now = time.time()
    #     if self.update_bullet_anim == True:
    #         #if now - self.bullet_last_update > self.bullet_frame_rate:
    #         self.bullet_last_update = now
    #         self.bullet_animation_index += 1
    #         if self.bullet_animation_index < len(self.bullet_anim) - 1:
    #             self.bullet = self.bullet_anim[self.bullet_animation_index]
    #         else:
    #             self.bullet = self.bullet_anim[self.bullet_animation_index]
    #             self.bullet_animation_index = 0
    #             self.update_bullet_anim = False
    #
    #     # if now - self.bullet_last_update > self.bullet_frame_rate:
    #     #     self.update_bullet_anim = False
    #
    # def draw_bullet(self, win, enemies):
    #     self.bullet = self.bullet_anim[self.bullet_animation_index]
    #
    #     enemy_group = []
    #     for en in enemies:
    #         if self.enemy_in_range(en):
    #             enemy_group.append(en)
    #
    #             x_en = enemy_group[0].x + enemy_group[0].width // 2
    #             y_en = enemy_group[0].y + enemy_group[0].height // 2
    #
    #             distance = ((x_en-self.x)**2 + (y_en-self.y)**2)**0.5
    #
    #             x_delta = (x_en - self.x) / 10
    #             y_delta = (y_en - self.y) / 10
    #
    #             x = self.x
    #             y = self.y
    #             x += x_delta
    #             y += y_delta
    #
    #             win.blit(self.bullet, (x, y))
    #
    #         elif not self.enemy_in_range(en) and enemy_group:
    #             enemy_group.pop(0)


    # def throw(self, enemies, tech_level):
    #     """
    #     if enemy is in range, throw the projectile (and reset the count)
    #     :param enemies: list
    #     :param tech_level: int
    #     :return: None
    #     """
    #     if not self.proj:
    #         for en in enemies:
    #             if self.enemy_in_range(en):
    #                 self.proj_count = 0
    #                 if en.x > self.x:
    #                     self.proj = [pygame.transform.flip(img, True, False) for img in self.proj_images[tech_level]]
    #                     self.proj_flip = True
    #                 else:
    #                     self.proj = self.proj_images[tech_level]
    #                     self.proj_flip = False
    #                 break
    #
    # def draw_projectile(self, win, flip):
    #     """
    #     draw the projectile
    #     """
    #     proj_x = self.x + 40 if flip else self.x - 40
    #     proj_y = self.y
    #     if self.proj_count < FPS and self.proj:
    #         img = self.proj[self.proj_count // 20]
    #         win.blit(img, (proj_x - img.get_width()//2, proj_y - img.get_height()//2))
    #         self.proj_count += 1
    #     else:
    #         self.proj = []

    def attack_anim(self, tech_level):
        now = time.time()
        if self.update_anim == True:
            if now - self.last_update > self.frame_rate[self.level["cool down"]]:
                self.last_update = now
                self.animation_index += 1
                if self.animation_index < len(self.animation)-1:
                    self.images[tech_level] = self.animation[self.animation_index]
                else:
                    self.images[tech_level] = self.animation[self.animation_index]
                    self.animation_index = 0
                    self.update_anim = False
                    self.update_bullet_anim = True

    def flip_image(self, enemies):
        enemy_group = []
        for en in enemies:
            if self.enemy_in_range(en):
                enemy_group.append(en)
                if enemy_group[0].x > self.x:       # 找到範圍內第一個敵人
                    self.update_flip = False
                else:
                    self.update_flip = True
            elif not self.enemy_in_range(en) and enemy_group:
                enemy_group.pop(0)

    # def throw(self, enemies, tech_level):
    #     """
    #     if enemy is in range, throw the projectile (and reset the count)
    #     :param enemies: list
    #     :param tech_level: int
    #     :return: None
    #     """
    #     if not self.proj:
    #         for en in enemies:
    #             if self.enemy_in_range(en):
    #                 self.proj_count = 0
    #                 if en.x > self.x:
    #                     self.proj = [pygame.transform.flip(img, True, False) for img in self.proj_images[tech_level]]
    #                     self.proj_flip = True
    #                 else:
    #                     self.proj = self.proj_images[tech_level]
    #                     self.proj_flip = False
    #                 break


    def draw_tower(self, win, tech_level):
        """
        draw the tower itself
        :param win: game window
        :param tech_level: int
        :return: None
        """
        if self.update_flip == True:
            self.images[tech_level] = pygame.transform.flip(self.animation[self.animation_index], True, False)
            win.blit(self.images[tech_level], (self.x - self.width // 2, self.y - self.height // 2))
        else:
            self.images[tech_level] = self.animation[self.animation_index]
            win.blit(self.images[tech_level], (self.x - self.width // 2, self.y - self.height // 2))


    def draw(self, win, tech_level):
        """
        draw the tower and other stuffs if the tower is selected
        :param win: obj
        :param tech_level: int
        :return: None
        """
        if self.menu:
            self.draw_range(win)
            self.menu.draw(win)
        self.draw_tower(win, tech_level)
        #self.draw_bullet(win)
        #self.draw_attack_anim(win, tech_level)
        #self.draw_attack_animation(win, tech_level)
        # self.draw_projectile(win, self.proj_flip)


    def draw_range(self, win):
        """
        draw the attack range of tower
        :param win: window
        :return:  None
        """
        tw_range = self.ability["range"][self.level["range"]]
        surface = pygame.Surface((tw_range * 2, tw_range * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, (128, 128, 128, 120), (tw_range, tw_range), tw_range)
        win.blit(surface, (self.x - tw_range, self.y - tw_range))


class UpgradeMenu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = menu_image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.buttons = [Button(self.x, self.y+75, "selling"),
                        Button(self.x, self.y-70, "range"),
                        Button(self.x+69, self.y+6, "damage"),
                        Button(self.x-69, self.y+6, "cool down"),
                        ]

    def is_clicked(self, x, y):
        if (self.x - self.width // 2) < x < (self.x + self.width // 2) \
                and (self.y - self.height // 2) < y < (self.y + self.height // 2):
            return True
        return False

    def draw(self, win):
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        for btn in self.buttons:
            btn.draw(win)

    def get_items(self, x, y):
        for btn in self.buttons:
            if btn.is_clicked(x, y):
                return btn.name


class Button:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.image = btn_image[self.name]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.is_selected = False

    def is_clicked(self, x, y):
        if (self.x - self.width // 2) < x < (self.x + self.width // 2) \
                and (self.y - self.height // 2) < y < (self.y + self.height // 2):
            return True
        return False

    def draw(self, win):
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))