import pygame
import os
from game import Game
import time

pygame.init()
pygame.mixer.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WIDTH, HEIGHT = 1024, 600
FPS = 60


start_anim = [pygame.transform.scale(pygame.image.load(os.path.join("image_2/start_menu/", f"start-btn-{i}.png")), (170, 65)) for i in range(1, 5)]
theme_anim = [pygame.transform.scale(pygame.image.load(os.path.join("image_2/start_menu/", f"start-{i}.png")), (983, 360)) for i in range(1, 5)]


class MainMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIDTH, HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("image_2/start_menu", "start_bg.png")), (WIDTH, HEIGHT))
        # button
        self.start_img = None
        self.start_anim = start_anim
        self.theme_img = None
        self.theme_anim = theme_anim
        self.animation_index = 0
        self.last_update = time.time()
        self.frame_rate = 0.1

        self.start_btn = Buttons(WIDTH//2-(170/2)-5, 450-5, 180, 75)  # x, y, width, height
        self.sound_btn = Buttons(857, 528, 65, 65)
        self.muse_btn = Buttons(938, 528, 65, 65)
        self.buttons = {"sound": self.sound_btn,
                        "muse": self.muse_btn,
                        "start": self.start_btn,
                        }
        # music and sound
        #self.sound = pygame.mixer.Sound("./sound/sound.flac")

    def play_music(self):
        pygame.mixer.music.load("./sound/menu.wav")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        #self.sound.set_volume(0.2)

    def update_animation(self):
        now = time.time()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.animation_index += 1
            if self.animation_index < len(self.start_anim) - 1:
                self.theme_img = self.theme_anim[self.animation_index-1]
                self.start_img = self.start_anim[self.animation_index]
            else:
                self.theme_img = self.theme_anim[self.animation_index - 1]
                self.start_img = self.start_anim[self.animation_index]
                self.animation_index = 0

    def draw(self, surf):
        surf.blit(self.bg, (0, 0))
        self.theme_img = self.theme_anim[self.animation_index]
        surf.blit(self.theme_img, (WIDTH // 2 - (983 / 2), 60))
        self.start_img = self.start_anim[self.animation_index]
        surf.blit(self.start_img, (WIDTH//2-(170/2), 450))

    def menu_run(self):
        run = True
        clock = pygame.time.Clock()
        pygame.display.set_caption("Fire Tower Defense Game")
        self.play_music()
        while run:
            clock.tick(FPS)

            self.update_animation()
            self.draw(self.menu_win)

            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if self.start_btn.get_touched(x, y):
                        #self.sound.play()
                        pygame.mixer.music.pause()
                        g = Game()
                        g.game_run()
                        run = False
                    elif self.muse_btn.get_touched(x, y):
                        pygame.mixer.music.pause()
                        #self.sound.play()
                    elif self.sound_btn.get_touched(x, y):
                        pygame.mixer.music.unpause()


            # while cursor is moving
            for name, btn in self.buttons.items():
                btn.create_frame(x, y)
                btn.draw_frame(self.menu_win)




            pygame.display.update()
        pygame.quit()


class Buttons:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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

    def draw_frame(self, surf):
        if self.frame:
            pygame.draw.rect(surf, WHITE, self.frame, 5)
