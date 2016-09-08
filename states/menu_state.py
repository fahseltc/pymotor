import pygame

import CONSTANTS
from log import log
from game_state import GameState
from visual_element import VisualElement, ClickableElement


class MenuState(GameState):
    def __str__(self):
        return "Menu"

    def __init__(self):
        self.font = pygame.font.Font(None, 16)
        self.square = VisualElement(100, 100, 100, 100, CONSTANTS.BLUE)
        self.square2 = ClickableElement(200, 100, 100, 100, CONSTANTS.GRAY)
        self.square2.on_hover(self.square2.highlight)
        self.gui_group = pygame.sprite.Group()
        self.gui_group.add(self.square)
        self.gui_group.add(self.square2)

    def update(self, dt):
        log(self.__class__.__name__).info("update:begin")


        self.square2.on_hover(self.square2.highlight)


        log(self.__class__.__name__).info("update:end")

    def render(self, screen):
        log(self.__class__.__name__).info("render:begin")

        self.square2.render_text("HAY LOTS OF LONG TEXT DOES IT WRAP OKASDASDASDAS", CONSTANTS.WHITE, 1)
        self.gui_group.draw(screen)


        log(self.__class__.__name__).info("render:end")

    def on_exit(self):
        log(self.__class__.__name__).info("on_exit:begin")
        log(self.__class__.__name__).info("on_exit:end")

    def on_enter(self):
        log(self.__class__.__name__).info("on_enter:begin")
        log(self.__class__.__name__).info("on_enter:end")


    def draw_background_rect(self, screen):
        self.gui_group.draw(screen)
        #screen.blit(self.square)
