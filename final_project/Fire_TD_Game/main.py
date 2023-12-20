import pygame
from start_menu import MainMenu


if __name__ == '__main__':
    pygame.init()
    main = MainMenu()
    main.menu_run()