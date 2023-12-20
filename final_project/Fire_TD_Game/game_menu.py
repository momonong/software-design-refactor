import pygame
import time
from builder import TowerBuilder

from color_setting import *

pygame.font.init()
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WIDTH = 1024
HEIGHT = 600


class Buttons:
    def __init__(self, x, y, image_icon=None, image=None):
        self.x = x
        self.y = y
        self.image_icon = image_icon
        self.image = image
        self.width = self.image_icon.get_width() if self.image_icon else 45
        self.height = self.image_icon.get_height() if self.image_icon else 45
        self.frame = None

    def get_touched(self, x, y):
        """
        if cursor position is on the button, return True
        :param x: int
        :param y: int
        :return: Bool
        """
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False

    def create_frame(self, x, y):
        """
        if cursor position is on the button, create button frame
        :param x: int
        :param y: int
        :return: None
        """
        if self.get_touched(x, y):
            self.frame = pygame.Rect(self.x, self.y, self.width, self.height)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame:
            pygame.draw.rect(win, WHITE, self.frame, 5)


class FunctionMenu:
    def __init__(self):
        # images
        # assets
        self.base_max_hp = 100
        # buttons
        self.sound_btn = Buttons(795, 545)
        self.muse_btn = Buttons(850, 545)
        self.continue_btn = Buttons(902, 545)
        self.pause_btn = Buttons(957, 545)
        self.buttons = {"sound": self.sound_btn,
                        "muse": self.muse_btn,
                        "continue": self.continue_btn,
                        "pause": self.pause_btn,
                        }
        # font
        self.font_size = 30
        #self.font = pygame.font.SysFont("comicsans", self.font_size)
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", self.font_size)
        # menu size
        self.width = WIDTH
        self.height = HEIGHT
        # time
        self.start_time = time.time()

    def draw(self, win, wave, tech_level, base_hp, money, game_time):
        """
        show all the information on the function menu
        :param win: window
        :param wave: int
        :param tech_level: int
        :param lives: int
        :param money: int
        :return: None
        """
        # level
        text = self.font.render(f"Wave: {wave}", True, WHITE)
        win.blit(text, (15, 10))

        # money
        text = self.font.render(f"Money: {money}", True, WHITE)
        win.blit(text, (15, 35))

        # tech level
        text = self.font.render(f"Level: {tech_level}", True, WHITE)
        win.blit(text, (905, 120))

        # draw_base_hp
        base_hp_height = 100 * (base_hp / self.base_max_hp)
        pygame.draw.rect(win, RED_1, [720, 30, 10, self.base_max_hp], 0)
        pygame.draw.rect(win, RED_2, [720, 130-base_hp_height, 10, base_hp_height], 0)

        # draw button frame
        for key, btn in self.buttons.items():
            btn.draw_frame(win)

        # draw time
        pygame.draw.rect(win, BLACK, [0, self.height - 40, 80, 40])
        minute = game_time // 60
        second = game_time % 60
        if second < 10:
            time_text = self.font.render(f"{minute}:0{second}", True, (255, 255, 255))
        else:
            time_text = self.font.render(f"{minute}:{second}", True, (255, 255, 255))
        time_rect = time_text.get_rect()
        time_rect.center = (40, self.height - 20)
        win.blit(time_text, time_rect)


class BuildMenu:
    def __init__(self):
        self.item_names = ["sandbag", "wiper", "pump"]
        # tower
        self.tower_images_icon = [pygame.transform.scale(pygame.image.load('image_2/Tower/Fireman/fireman-icon.png'), (int(278/2.5), int(246/2.5))),
                             pygame.transform.scale(pygame.image.load('image_2/Tower/FireTruck/firetruck-icon.png'), (int(278/2.5), int(246/2.5))),
                             pygame.transform.scale(pygame.image.load('image_2/Tower/FireExtinguisher/fireextinguisher-icon.png'), (int(278/2.5), int(246/2.5))),
                             ]
        self.tower_images = [
            pygame.transform.scale(pygame.image.load('image_2/Tower/Fireman/fireman-0.png'), (int(466//3.5), int(260//3.5))),
            pygame.transform.scale(pygame.image.load('image_2/Tower/FireTruck/firetruck-0.png'), (int(513/3), int(220/3))),
            pygame.transform.scale(pygame.image.load('image_2/Tower/FireExtinguisher/fireextinguisher-0.png'), (int(360/3), int(260/3))),
            ]
        self.tower_buttons = {"sandbag": Buttons(920, 150, self.tower_images_icon[0], self.tower_images[0]),
                              "wiper": Buttons(920, 240, self.tower_images_icon[1], self.tower_images[1]),
                              "pump": Buttons(920, 330, self.tower_images_icon[2], self.tower_images[2])
                              }
        self.tower_market_price = {"sandbag": 120,
                                   "wiper": 120,
                                   "pump": 120,
                                   }
        # tech
        self.upgrade_image = pygame.transform.scale(pygame.image.load("image/game_menu/upgrade.png"), (100, 45))
        self.upgrade_button = Buttons(920, 440, self.upgrade_image)
        self.upgrade_market_price = [300, 1000, 1500]

    def draw(self, win):
        win.blit(self.upgrade_button.image_icon, (self.upgrade_button.x, self.upgrade_button.y))
        for name, btn in self.tower_buttons.items():
            win.blit(btn.image_icon, (btn.x, btn.y))


    def get_items(self, x, y):
        """
        if the cursor is on the tower button (while clicked), call out the tower builder
        :param x: int
        :param y: int
        :return: item object
        """
        for name, btn in self.tower_buttons.items():
            if btn.get_touched(x, y):
                return TowerBuilder(x, y, btn.image, name, self.tower_market_price[name])

    def upgrade_tech_level(self, x, y, tech_level, money):
        """
        if the cursor is on the upgrade buttons (while clicked), upgrade the technology level and pay for it
        :param x: int
        :param y: int
        :param tech_level: int
        :param money: int
        :return: (int, int, str)
        """
        notice = None
        if self.upgrade_button.get_touched(x, y):
            if tech_level >= 2:
                notice = f"Already the highest level"
            elif money < self.upgrade_market_price[tech_level]:
                notice = f"{self.upgrade_market_price[tech_level]} is needed for upgrade"
            else:
                money -= self.upgrade_market_price[tech_level]
                notice = f"Pay {self.upgrade_market_price[tech_level]} to upgrade technology level"
                tech_level += 1
        return tech_level, money, notice



