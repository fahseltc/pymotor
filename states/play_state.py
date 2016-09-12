import pygame

import CONSTANTS
from log import log
from game_state import GameState


class PlayState(GameState):
    def __str__(self):
        return "Play"

    def __init__(self, state_machine):
        self.state_machine = state_machine

    def update(self, dt):
        log(self.__class__.__name__).info("update:begin")
        log(self.__class__.__name__).info("update:end")

    def render(self, screen):
        log(self.__class__.__name__).info("render:begin")
        screen.fill(CONSTANTS.BLACK)
        log(self.__class__.__name__).info("render:end")

    def on_exit(self):
        log(self.__class__.__name__).info("on_exit:begin")
        log(self.__class__.__name__).info("on_exit:end")

    def on_enter(self):
        log(self.__class__.__name__).info("on_enter:begin")
        log(self.__class__.__name__).info("on_enter:end")
