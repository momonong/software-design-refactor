import pygame
from setting import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE
from color_setting import *


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font_size = 30
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", self.font_size)

    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE, (0, 0))

    def draw_enemies(self, enemies):
        for en in enemies.get():
            self.win.blit(en.image, en.rect)
            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(self.win, RED_1, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, RED_2, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def draw_towers(self, towers):
        # draw tower
        for tw in towers:
            tw.image = tw.animation[tw.animation_index]
            self.win.blit(tw.image, tw.rect)

    def draw_range(self, selected_tower):
        # draw tower range
        if selected_tower is not None:
            tw = selected_tower
            # create a special surface that is able to render semi-transparent image
            surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
            transparency = 120
            pygame.draw.circle(surface, (128, 128, 128, transparency), tw.rect.center, tw.range)
            self.win.blit(surface, (0, 0))

    def draw_menu(self, menu):
        self.win.blit(menu.image, menu.rect)
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_main_menu(self, menu):
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

            x, y = pygame.mouse.get_pos()
            btn.create_frame(x, y)
            btn.draw_frame(self.win)

    def draw_plots(self, plots):
        for pt in plots:
            self.win.blit(pt.image, pt.rect)

    def draw_money(self, money: int):
        """ (Q2.1)render the money"""
        text = self.font.render(f"Money: {money}", True, (255, 255, 255))
        self.win.blit(text, (5, 45))

    def draw_wave(self, wave: int):
        """(Q2.2)render the wave"""
        text = self.font.render(f"Wave: {wave}", True, (255, 255, 255))
        self.win.blit(text, (5, 15))

    def draw_hp(self, model):
        # draw base_hp
        base_max_hp = model.max_hp
        base_hp_height = 100 * (model.hp / base_max_hp)
        pygame.draw.rect(self.win, RED_1, [720, 30, 10, base_max_hp], 0)
        pygame.draw.rect(self.win, RED_2, [720, 130 - base_hp_height, 10, base_hp_height], 0)







