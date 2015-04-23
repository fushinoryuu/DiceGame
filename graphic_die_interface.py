# graphic_die_interface.py
# Christian Munoz
# 03/13/2015

import pygame
from pygame.locals import *
from graphic_die_class import GraphicDie
from button_class import SimpleButton
from game_rules_class import GameRules


class GraphicDieInterface:

    def __init__(self):
        pygame.init()

        self.number_of_dice = 7

        self.display_width = 640
        self.display_height = 480

        self.display_surface = pygame.display.set_mode((self.display_width, self.display_height), 0, 32)
        pygame.display.set_caption('Dice Game')

        #RGB colors for later use
        self.rust = (151, 47, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.dark_turquoise = (0, 64, 51)
        self.lite_turquoise = (0, 164, 151)
        self.orange = (176, 67, 17)
        self.grey = (50, 50, 50)
        self.background_color = (0, 147, 134)
        self.display_surface.fill(self.background_color)

        self.die_size = self.display_width//(self.number_of_dice + 3)
        self.die_gap = self.die_size//(self.number_of_dice + 1)
        self.die_y = self.display_height//4
        self.die_object_list = []
        self.xPT = 0
        self.die_x = []

        for x in range(self.number_of_dice):
            self.die_x.append(self.xPT + self.die_size + self.die_gap)
            self.xPT = self.xPT + self.die_size + self.die_gap

        for i in range(self.number_of_dice):
            self.die_object_list.append(GraphicDie(self.die_size, self.display_surface, (self.die_x[i], self.die_y)))

        b_width = self.display_width//5
        b_height = b_width//4
        b_x_position = self.display_width//2 - b_width//2
        b_y_position = int(self.die_y + self.die_size * 1.25)
        b_position = (b_x_position, b_y_position)
        self.b1 = SimpleButton(b_width, b_height, self.orange, self.grey, "Roll Dice", self.display_surface, b_position)
        self.b2 = SimpleButton(b_width, b_height, self.orange, self.grey, "Second Roll", self.display_surface, b_position)
        self.b3 = SimpleButton(b_width, b_height, self.orange, self.grey, "Third Roll", self.display_surface, b_position)
        self.b4 = SimpleButton(b_width, b_height, self.orange, self.grey, "Last Roll", self.display_surface, b_position)
        self.b5 = SimpleButton(b_width, b_height, self.orange, self.grey, "Play Again", self.display_surface, b_position)
        self.buttons_list = [self.b1, self.b2, self.b3, self.b4, self.b5]

        self.game_font = pygame.font.SysFont("Broadway", 128)
        self.instructions_text = "Click on Dice -- Red to Roll, White to Hold"
        self.title_surface = self.game_font.render("Dice Game", True, self.dark_turquoise, None)
        self.instruction_surface = self.game_font.render(self.instructions_text, True, self.lite_turquoise, None)
        self.instruction_surface = pygame.transform.scale(self.instruction_surface, (self.display_width - (self.display_width//5), self.display_width//20))

        self.game_rules = GameRules()
        self.score_active = False
        self.instruction_active = False

    def all_dice_active(self):
        for i in self.die_object_list:
            i.ACTIVE = True

    def all_dice_inactive(self):
        for i in self.die_object_list:
            i.ACTIVE = False

    def all_dice_hold(self):
        for i in self.die_object_list:
            i.HOLD = True

    def all_dice_roll(self):
        for i in self.die_object_list:
            i.HOLD = False

    def set_value(self):
        """Sets all not HOLD Die to a new random value."""
        for x in self.die_object_list:
            if not x.HOLD:
                x.set_random_value()

    def fill_gradient(self, surface, color, gradient, rect=None, vertical=True, forward=True):
        """fill a surface with a gradient pattern
        Parameters:
        color -> starting color
        gradient -> final color
        rect -> area to fill; default is surface's rect
        vertical -> True=vertical; False=horizontal
        forward -> True=forward; False=reverse

        Pygame recipe: http://www.pygame.org/wiki/GradientCode"""
        if rect is None: rect = surface.get_rect()
        x1,x2 = rect.left, rect.right
        y1,y2 = rect.top, rect.bottom
        if vertical:
            h = y2-y1
        else:
            h = x2-x1
        if forward:
            a, b = color, gradient
        else:
            b, a = color, gradient
        rate = (
            float(b[0]-a[0])/h,
            float(b[1]-a[1])/h,
            float(b[2]-a[2])/h
        )
        fn_line = pygame.draw.line
        if vertical:
            for line in range(y1,y2):
                color = (
                    min(max(a[0]+(rate[0]*(line-y1)),0),255),
                    min(max(a[1]+(rate[1]*(line-y1)),0),255),
                    min(max(a[2]+(rate[2]*(line-y1)),0),255)
                )
                fn_line(surface, color, (x1,line), (x2,line))
        else:
            for col in range(x1,x2):
                color = (
                    min(max(a[0]+(rate[0]*(col-x1)),0),255),
                    min(max(a[1]+(rate[1]*(col-x1)),0),255),
                    min(max(a[2]+(rate[2]*(col-x1)),0),255)
                )
                fn_line(surface, color, (col,y1), (col,y2))

    def display_dice(self):
        """This function will display all dice."""
        self.fill_gradient(self.display_surface, self.black, self.white)
        self.die1.display_die()
        self.die2.display_die()
        self.die3.display_die()
        self.die4.display_die()
        self.die5.display_die()

    def display_text(self):
        """This functions displays all the text on the game."""
        self.display_surface.blit(self.label, (self.half_x - (len( self.text)/2), self.half_y/2))

    def display_interface(self):
        """This functions displays everything that needs to go on the display surface."""
        #self.display_text()
        self.display_dice()