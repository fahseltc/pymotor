import pygame

from log import log
import CONSTANTS
from game_state import GameState


class QuitState(GameState):
    def __str__(self):
        return "Menu"

    def update(self, dt):
        pass

    def render(self, screen):
        pass

    def on_exit(self):
        pass

    def on_enter(self):
        log(self.__class__.__name__).info("on_enter:begin")
        CONSTANTS.RUNNING = False
        #log(self.__class__.__name__).info("on_enter:end")
