import pygame

import CONSTANTS
from log import log

class VisualElement(pygame.sprite.Sprite): #visual element?
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.text = TextElement()

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def highlight(self):
        r = self.color[0]+30 if self.color[0] < 225 else self.color[0]
        g = self.color[1]+30 if self.color[1] < 225 else self.color[1]
        b = self.color[2]+30 if self.color[2] < 225 else self.color[2]

        #highlighted = [x+30 for x in self.color if x < 225]
        #print(highlighted)
        self.image.fill((r,g,b))

    def update(self):
        if self.text.text is not 'Default':
            self.render_text()

    # def render_text(self, text, position=False):
    #     if position:
    #         self.text.position = position
    #     else:
    #         self.text.position = (0,0)
    #     self.text.text = text
    #     font = pygame.font.Font(None, 20)
    #     #rendered_text = TextBounds.render("STRING", font, rect, colortext, colorbg, justification )
    #     #rendered_text = font.render(self.text.text, False, CONSTANTS.WHITE)
    #     self.image.blit(rendered_text, self.text.position)


    # justification - 0 (default) left-justified
    #                     1 horizontally centered
    #                     2 right-justified

    def render_text(self, color=CONSTANTS.WHITE, justification=1):

        font = pygame.font.Font(None, self.text.size)
        final_lines = []

        requested_lines = self.text.text.splitlines()
        for requested_line in requested_lines:
            if font.size(requested_line)[0] > self.rect.width:
                words = requested_line.split(' ')
                # if any of our words are too long to fit, return.
                for word in words:
                    if font.size(word)[0] >= self.rect.width:
                        pass
                # Start a new line
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    # Build the line while the words fit.
                    if font.size(test_line)[0] < self.rect.width:
                        accumulated_line = test_line
                    else:
                        final_lines.append(accumulated_line)
                        accumulated_line = word + " "
                final_lines.append(accumulated_line)
            else:
                final_lines.append(requested_line)

        # NOW DRAW DAT
        surface = self.image

        accumulated_height = 5
        for line in final_lines:
            if accumulated_height + font.size(line)[1] >= self.rect.height:
                raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
            if line != "":
                tempsurface = font.render(line, 1, color)
                if justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((self.rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (self.rect.width - tempsurface.get_width(), accumulated_height))

            accumulated_height += font.size(line)[1]

class ClickableElement(VisualElement):
    """
    A GUI class for handling mouse interaction
    """
    def __init__(self, x, y, width, height, color):
        VisualElement.__init__(self, x, y, width, height, color)
        self.click_function = None
        self.hover_function = None

    def set_hover_function(self, function):
        self.hover_function = function

    def set_click_function(self, function):
        self.click_function = function

    def update(self):
        self.on_hover()
        self.on_click()
        super(ClickableElement, self).update()

    def on_hover(self):
        if self.hover_function is not None:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                log(self.__class__.__name__).info("on_hover:enter")
                self.hover_function()

    def on_click(self):
        if self.click_function is not None:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                log(self.__class__.__name__).info("on_click:enter")
                self.click_function()

class TextElement(pygame.font.Font):
    def __init__(self, text='Default', size=80, position=(0,0)):
        self.text = text
        self.size = size
        #self.position = position
