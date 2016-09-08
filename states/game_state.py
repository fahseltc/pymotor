from abc import ABCMeta, abstractmethod

from log import log


class GameState:
    __metaclass__ = ABCMeta
    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    @abstractmethod
    def on_exit(self):
        pass

    @abstractmethod
    def on_enter(self):
        pass


class EmptyState(GameState):
    def __str__(self):
        return "Empty"

    def update(self, dt):
        log(self.__class__.__name__).info("update:begin")
        log(self.__class__.__name__).info("update:end")

    def render(self, screen):
        log(self.__class__.__name__).info("render:begin")
        log(self.__class__.__name__).info("render:end")

    def on_exit(self):
        log(self.__class__.__name__).info("on_exit:begin")
        log(self.__class__.__name__).info("on_exit:end")

    def on_enter(self):
        log(self.__class__.__name__).info("on_enter:begin")
        log(self.__class__.__name__).info("on_enter:end")
