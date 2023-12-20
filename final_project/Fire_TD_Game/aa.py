import pygame

WIDTH = 500
HEIGHT = 600
FPS = 60

# 遊戲初始化
pygame.init()

# 遊戲視窗
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My First Game')

# 遊戲迴圈
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update game

    # display

    pygame.display.update()

pygame.quit()
