import pygame
from pygame.locals import *

from log import log, setup_logs
from states.game_state import GameState, EmptyState
from states.menu_state import MenuState
from states.play_state import PlayState
from states.state_machine import StateMachine
import CONSTANTS


setup_logs()



pygame.init()
#pygame.display.set_caption(CONSTANTS.TITLE)
pygame.display.set_mode(CONSTANTS.RESOLUTION,RESIZABLE)

state_machine = StateMachine()

menu_state = MenuState(state_machine)
state_machine.add_state(str(menu_state), menu_state)
state_machine.set_state(str(menu_state))

play_state = PlayState(state_machine)
state_machine.add_state(str(play_state), play_state)


log("root").info("done_setup")

screen = pygame.display.get_surface()
clock = pygame.time.Clock()


while(CONSTANTS.RUNNING):
    log("root").info("loop start")
    log("root").info("%s" % CONSTANTS.RUNNING)

    dt = clock.tick(60)/1000.

    #event = pygame.event.wait()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            CONSTANTS.RUNNING = False
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                CONSTANTS.RUNNING = False
        elif event.type == VIDEORESIZE:
            CONSTANTS.RESOLUTION = (event.w,event.h)
            pygame.display.set_mode(CONSTANTS.RESOLUTION,RESIZABLE)
            pygame.display.update()

    state_machine.update(dt)
    state_machine.render(screen)

    pygame.display.flip()
    log("root").info("%d , %d" % (CONSTANTS.RESOLUTION[0],CONSTANTS.RESOLUTION[1]))

    log("root").info("loop end")
    log("root").info("---------------------------------------------------------")

