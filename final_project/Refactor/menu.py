import pygame
import os
from color_setting import *

pygame.init()

menu_image = pygame.transform.scale(pygame.image.load(os.path.join("image/Upgrade_Menu", "upgrade_menu.png")), (160, 160))
damage_btn_image = pygame.transform.scale(pygame.image.load(os.path.join("image/Upgrade_Menu", "damage.png")), (35, 35))
range_btn_image = pygame.transform.scale(pygame.image.load(os.path.join("image/Upgrade_Menu", "range.png")), (33, 33))
cd_time_btn_image = pygame.transform.scale(pygame.image.load(os.path.join("image/Upgrade_Menu", "cd_time.png")), (40, 33))
sell_btn_image = pygame.transform.scale(pygame.image.load(os.path.join("image/Upgrade_Menu", "sell.png")), (35, 35))

fireman_btn_image = pygame.transform.scale(pygame.image.load(os.path.join("image/Tower/Fireman", "fireman-5.png")), (int(466/6.5), int(260/6.5)))
firetruck_btn_image = pygame.transform.scale(pygame.image.load(os.path.join("image/Tower/FireTruck", "firetruck-5.png")), (int(513/6.5), int(220/6.5)))
extinguisher_btn_image = pygame.transform.scale(pygame.image.load(os.path.join("image/Tower/FireExtinguisher", "fireextinguisher-3.png")), (int(360/6.5), int(260/6.5)))

mute_button_image = pygame.transform.scale(pygame.image.load("image/mute.png"), (45, 45))
music_button_image = pygame.transform.scale(pygame.image.load("image/sound.png"), (45, 45))
continue_button_image = pygame.transform.scale(pygame.image.load("image/continue.png"), (45, 45))
pause_button_image = pygame.transform.scale(pygame.image.load("image/pause.png"), (45, 45))


class Button:
    def __init__(self, image, name: str, x: int, y: int):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        return True if self.rect.collidepoint(x, y) else False

    @property
    def response(self):
        return self.name

    def create_frame(self, x: int, y: int):
        """if cursor position is on the button, create button frame"""
        if self.clicked(x, y):
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 10)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, WHITE, self.frame, 3)


class Menu:
    def __init__(self, x: int, y: int):
        self.image = menu_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._buttons = []

    @property
    def buttons(self):
        return self._buttons


class UpgradeMenu(Menu):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._buttons = [Button(damage_btn_image, "damage", self.rect.centerx-55, self.rect.centery-52),
                         Button(range_btn_image, "range", self.rect.centerx+54, self.rect.centery-52),
                         Button(cd_time_btn_image, "cd_time", self.rect.centerx-54, self.rect.centery+55),
                         Button(sell_btn_image, "sell", self.rect.centerx+55, self.rect.centery+55)]


class BuildMenu(Menu):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._buttons = [Button(fireman_btn_image, "fireman", self.rect.centerx-55, self.rect.centery-52),
                         Button(firetruck_btn_image, "firetruck", self.rect.centerx+54, self.rect.centery-52),
                         Button(extinguisher_btn_image, "extinguisher", self.rect.centerx-54, self.rect.centery+55)]


class MainMenu():
    def __init__(self):
        self._buttons = [Button(music_button_image, "music", 795, 570),
                         Button(mute_button_image, "mute", 850, 570),
                         Button(continue_button_image, "continue", 902, 570),
                         Button(pause_button_image, "pause", 957, 570)]

    @property
    def buttons(self):
        return self._buttons


