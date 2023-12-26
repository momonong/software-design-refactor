import pygame


# controller
class GameController:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       "keyboard key": 0,
                       "pause": False
                       }
        self.request = None  # response of user input

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.call_menu()
        self.model.towers_attack()
        self.model.enemies_advance()

    def update_user_request(self):
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.call_menu()

    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       "keyboard key": None,
                       "pause": False
                       }
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player press action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    self.events["keyboard key"] = pygame.K_n
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

        if self.model.is_pause:
            self.events["pause"] = True
        else:
            self.events["pause"] = False

    def update_view(self):
        # render background
        self.view.draw_bg()
        self.view.draw_hp(self.model)
        self.view.draw_enemies(self.model.enemies)
        self.view.draw_towers(self.model.towers)
        self.view.draw_range(self.model.selected_tower)
        self.view.draw_plots(self.model.plots)

        if self.model.menu is not None:
            self.view.draw_menu(self.model.menu)

        self.view.draw_main_menu(self.model.main_menu)

        """(Q2) Controller request View to render something"""
        self.view.draw_wave(self.model.wave)
        self.view.draw_money(self.model.money)


    @property
    def quit_game(self):
        return self.events["game quit"]

    @property
    def is_pause(self):
        return self.events["pause"]


