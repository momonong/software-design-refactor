import pygame
import os
import time
from game import Game
from color_setting import *
from setting import WIN_WIDTH, WIN_HEIGHT, FPS

pygame.init()
pygame.mixer.init()

start_anim = [pygame.transform.scale(pygame.image.load(os.path.join("image/Start_Menu", f"start-btn-{i}.png")), (170, 65)) for i in range(1, 5)]
theme_anim = [pygame.transform.scale(pygame.image.load(os.path.join("image/Start_Menu", f"start-{i}.png")), (983, 360)) for i in range(1, 5)]


class StartMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("image/Start_Menu", "start_bg.png")), (WIN_WIDTH, WIN_HEIGHT))
        # button
        self.start_img = None
        self.start_anim = start_anim
        self.theme_img = None
        self.theme_anim = theme_anim
        self.animation_index = 0
        self.last_update = time.time()
        self.frame_rate = 0.1

        self.start_btn = Buttons(WIN_WIDTH//2-(170/2)-5, 450-5, 180, 75)  # x, y, width, height
        self.sound_btn = Buttons(857, 528, 65, 65)
        self.mute_btn = Buttons(938, 528, 65, 65)
        self.buttons = [self.sound_btn,
                        self.mute_btn,
                        self.start_btn]

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
        surf.blit(self.theme_img, (WIN_WIDTH // 2 - (983 / 2), 60))
        self.start_img = self.start_anim[self.animation_index]
        surf.blit(self.start_img, (WIN_WIDTH//2-(170/2), 450))


    def menu_run(self):
        run = True
        clock = pygame.time.Clock()
        pygame.display.set_caption("Flood Tower Defense Game")
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
                    if self.start_btn.clicked(x, y):
                        #self.sound.play()
                        game = Game()
                        game.run()
                        run = False
                    """(Q1.1) music on/off according to the button"""
                    # (hint) pygame.mixer.music.pause/unpause
                    if self.sound_btn.clicked(x, y):
                        pygame.mixer.music.unpause()
                    if self.mute_btn.clicked(x, y):
                        pygame.mixer.music.pause()

            # while cursor is moving (not click)
            """(Q1.2) create button frame and draw"""
            # (hint) use a for loop to go through all the buttons, create the frame, and draw it.
            for btn in self.buttons:
                btn.create_frame(x, y)
                btn.draw_frame(self.menu_win)

            pygame.display.update()
        pygame.quit()


class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = None

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False

    def create_frame(self, x: int, y: int):
        """if cursor position is on the button, create button frame"""
        if self.clicked(x, y):
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 10)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, WHITE, self.frame, 5)
