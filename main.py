import pygame
from pygame.locals import *

from log import log, setup_logs
from states.game_state import GameState, EmptyState
from states.menu_state import MenuState
from states.state_machine import StateMachine
import CONSTANTS


setup_logs()



pygame.init()
#pygame.display.set_caption(CONSTANTS.TITLE)
pygame.display.set_mode(CONSTANTS.RESOLUTION,RESIZABLE)

state_machine = StateMachine()
state_machine.update(1)
#state_machine.render()

state_machine.add_state(str(EmptyState()), EmptyState())
state_machine.set_state(str(EmptyState()))
state_machine.update(1)
#state_machine.render()

state_machine.add_state(str(MenuState()), MenuState())
state_machine.set_state(str(MenuState()))
state_machine.update(1)
#state_machine.render()

log("root").info("done_setup")

screen = pygame.display.get_surface()
clock = pygame.time.Clock()
running = True

while(running):
    log("root").info("loop start")

    dt = clock.tick(60)/1000.

    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        running = False
    elif event.type == KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False
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

