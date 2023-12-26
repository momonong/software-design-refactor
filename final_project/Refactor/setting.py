import pygame
import os

# game window
WIN_WIDTH = 1024
WIN_HEIGHT = 600

# Frame Per Second
FPS = 60

# path
PATH = [(3, 155), (17, 155), (44, 155), (73, 155), (111, 156),
        (143, 156), (183, 155), (211, 155), (238, 157), (269, 160),
        (290, 170), (304, 184), (316, 209), (323, 244), (327, 278),
        (325, 307), (324, 340), (324, 377), (325, 406), (331, 434),
        (347, 444), (370, 452), (395, 450), (422, 452), (444, 452),
        (471, 453), (501, 453), (531, 456), (562, 456), (587, 452),
        (610, 452), (636, 452), (669, 449), (681, 442), (692, 433),
        (696, 414), (698, 391), (703, 371), (718, 356), (737, 343),
        (765, 330), (794, 329), (822, 326), (842, 324), (857, 315),
        (873, 296), (877, 276), (877, 255), (877, 234), (876, 213),
        (876, 188), (878, 171), (878, 150), (878, 133), (878, 115)]

# base
BASE = pygame.Rect(740, 30, 270, 100)
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("image", "background.png")), (1024, 600))