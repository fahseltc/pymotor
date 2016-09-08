from game_state import EmptyState
from log import log

class StateMachine:

    def __init__(self):
        self.states = dict()
        self.current_state = EmptyState()

    def update(self, dt):
        self.current_state.update(dt)

    def render(self, screen):
        self.current_state.render(screen)

    def set_state(self, state_name):
        log(self.__class__.__name__).info("set_state: |old:%s -- new:%s|", str(self.current_state), state_name)
        self.current_state.on_exit()
        self.current_state = self.states[state_name]
        self.current_state.on_enter()

    def add_state(self, state_name, state):
        log(self.__class__.__name__).info("add_state:%s", state_name)
        self.states[state_name] = state
