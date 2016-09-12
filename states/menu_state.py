import sys
import pygame

import CONSTANTS
from log import log
from game_state import GameState, EmptyState
from visual_element import VisualElement, ClickableElement
from state_machine import StateMachine


class MenuState(GameState):
    def __str__(self):
        return "Menu"

    def __init__(self, state_machine):
        self.state_machine = state_machine

        self.font = pygame.font.Font(None, 16)

        # Make title text
        self.title = VisualElement(CONSTANTS.RESOLUTION[0] / 2 - 200, 20, 400, 70, CONSTANTS.DARKGRAY)
        self.title.text.text = "GAME TITLE"
        self.title.text.size = 90

        # Make play button
        self.play_button = ClickableElement(CONSTANTS.RESOLUTION[0] / 2 - 150, 400, 300, 80, CONSTANTS.DARKGRAY)
        self.play_button.text.text = "PLAY"
        self.play_button.set_hover_function(lambda : self.play_button.highlight)
        self.play_button.set_click_function(lambda : self.state_machine.set_state("Play"))

        # Make quit button
        self.exit_button = ClickableElement(CONSTANTS.RESOLUTION[0] / 2 - 150, 600, 300, 80, CONSTANTS.DARKGRAY)
        self.exit_button.text.text = "EXIT"
        self.exit_button.set_hover_function(lambda : self.exit_button.highlight)
        self.exit_button.set_click_function(lambda : self.state_machine.set_state("Quit"))

        self.gui_group = pygame.sprite.Group()

        self.gui_group.add(self.title)
        self.gui_group.add(self.exit_button)
        self.gui_group.add(self.play_button)


# Abstract base class methods

    def update(self, dt):
        log(self.__class__.__name__).info("update:begin")

        for element in self.gui_group:
            element.update()

        log(self.__class__.__name__).info("update:end")

    def render(self, screen):
        log(self.__class__.__name__).info("render:begin")

        self.gui_group.draw(screen)

        log(self.__class__.__name__).info("render:end")

    def on_exit(self):
        log(self.__class__.__name__).info("on_exit:begin")
        log(self.__class__.__name__).info("on_exit:end")

    def on_enter(self):
        log(self.__class__.__name__).info("on_enter:begin")
        log(self.__class__.__name__).info("on_enter:end")

# END Abstract base class methods


    def draw_background_rect(self, screen):
        self.gui_group.draw(screen)
