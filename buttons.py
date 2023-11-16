from graphics import *
from variables import *


class Button:
    def __init__(self,
                 func,
                 x_pos,
                 y_pos,
                 width,
                 height,
                 text,
                 font_size=40,
                 border_color="#FFFFFF",
                 text_color="#FFFFFF",
                 highlight_color="#FF0000",
                 border_width=3,
                 y_offset=11,
                 value=None):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.border_color = border_color
        self.text_color = text_color
        self.highlight_color = highlight_color
        self.thickness = border_width
        self.y_offset = y_offset
        self.font = pygame.font.Font("./Assets/Graphics/BebasNeue.ttf", size=font_size)
        self.text = self.font.render(text, True, self.text_color)
        self.command = func
        self.value = value

    def check_mouseover(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (self.x_pos <= mouse_x <= self.x_pos + self.width) and (self.y_pos <= mouse_y <= self.y_pos + self.height):
            return True
        return False

    def draw(self):
        self.check_mouseover()
        if self.check_mouseover() and not ((game.state == "Drawing cards" and game.current_turn == "Dealer")
                                           or game.state == "Card animation"
                                           or game.player_is_done and not game.state == "Summary"):
            pygame.draw.rect(screen, self.highlight_color, (self.x_pos, self.y_pos, self.width, self.height))
        pygame.draw.rect(screen, self.border_color, (self.x_pos, self.y_pos, self.width, self.height), self.thickness)
        screen.blit(self.text, (self.x_pos + self.width // 2 - self.text.get_width() // 2, self.y_pos + self.y_offset))

    def run_command(self):
        if self.check_mouseover():
            if not self.value:
                self.command()
            else:
                self.command(self.value)
