# graphic_die_interface.py
# Christian Munoz
# 04/24/2015

import pygame
from pygame.locals import *
from graphic_die_class import GraphicDie
from button_class import SimpleButton
from game_rules_class import GameRules

pygame.init()


class GraphicDieInterface:
    """This class defines the interface for the game."""
    def __init__(self):
        self.number_of_dice = 7

        self.display_width = 640
        self.display_height = 480

        self.background_image = pygame.image.load('background.png')
        self.lose_image = pygame.image.load('youlose.png')

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
        self.yellow = (192, 150, 24)
        self.background_color = (0, 147, 134)

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
        self.b5 = SimpleButton(b_width, b_height, self.orange, self.grey, "Next Round", self.display_surface, b_position)
        self.b6 = SimpleButton(b_width, b_height, self.orange, self.grey, "New Game", self.display_surface,
                               (b_position[0] - 150, b_position[1]))
        self.b7 = SimpleButton(b_width, b_height, self.orange, self.grey, "Quit", self.display_surface,
                               (b_position[0] + 150, b_position[1]))
        self.buttons_list = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7]

        self.game_font = pygame.font.SysFont("Magneto", 100)
        self.instructions_text = "Click on Dice -- Red to Roll, White to Hold"
        self.title_surface = self.game_font.render("Dice Game", True, self.dark_turquoise, None)
        self.instruction_surface = self.game_font.render(self.instructions_text, True, self.white, None)
        self.instruction_surface = pygame.transform.scale(self.instruction_surface, (self.display_width -
                                                                                     (self.display_width//5),
                                                                                     self.display_width//20))

        self.game_rules = GameRules()
        self.score_active = False
        self.instruction_active = False

    def all_dice_active(self):
        """Sets all the dice to active status."""
        for i in self.die_object_list:
            i.ACTIVE = True

    def all_dice_inactive(self):
        """Makes all the dice in the list inactive."""
        for i in self.die_object_list:
            i.ACTIVE = False

    def all_dice_hold(self):
        """Holds all the dice on the list."""
        for i in self.die_object_list:
            i.HOLD = True

    def all_dice_roll(self):
        """Rolls all the dice in the list."""
        for i in self.die_object_list:
            i.HOLD = False

    def set_value(self):
        """Sets all not HOLD Die to a new random value."""
        for x in self.die_object_list:
            if not x.HOLD:
                x.set_random_value()

    def all_buttons_inactive(self):
        """Make all buttons in list inactive."""
        for i in self.buttons_list:
            i.active = False

    def start_setup(self):
        """This function starts the set up for the game setting up the buttons and dice."""
        self.all_buttons_inactive()
        self.b1.active = True
        self.b6.active = True
        self.b7.active = True
        self.all_dice_inactive()
        self.all_dice_roll()

    def add_points(self):
        """Adds up the points from your final roll to the players current score."""
        self.score_tuple = self.game_rules.score_dice(self.die_object_list)
        self.game_rules.points += self.score_tuple[1]

    def change_points(self, change):
        """Helper function to change the score."""
        self.game_rules.points += change

    def reset_points(self, change):
        """Helper function to reset the points to 100."""
        self.game_rules.points = change

    def display_score(self):
        """Displays the score that player has for the current set of dice."""
        if self.score_active:
            score_string = self.score_tuple[0] + ', ' + 'You win' + str(self.score_tuple[1]) + ' Points'
            self.score_surface = self.game_font.render(score_string, True, self.yellow, None)
            self.score_surface = pygame.transform.scale(self.score_surface, (self.display_width - (self.display_width//3),
                                                                             self.display_height//10))
            w, h = self.score_surface.get_size()
            self.score_x = (self.display_width - w)//2
            self.score_y = int(self.die_y + self.die_size * 1.8)
            self.display_surface.blit(self.score_surface, (self.score_x, self.score_y + 20))

    def display_points(self):
        """Displays the points players current total score."""
        point_string = "Player's Points: " + str(self.game_rules.points)
        points_surface = self.game_font.render(point_string, True, self.rust, None)
        points_surface = pygame.transform.scale(points_surface, (self.display_width - (self.display_width//3),
                                                                 self.display_height//10))
        w, h = points_surface.get_size()
        points_x = (self.display_width - w)//2
        points_y = self.display_height - self.display_height//5
        self.display_surface.blit(points_surface, (points_x, points_y))

    def display_text(self):
        """This functions displays all the text on the game."""
        w, h = self.title_surface.get_size()
        text_x = (self.display_width - w)//2
        text_y = self.display_height//20
        self.display_surface.blit(self.title_surface, (text_x, text_y - 10))
        if self.instruction_active:
            temp_w, temp_h = self.instruction_surface.get_size()
            temp_x = (self.display_width - temp_w)//2
            temp_y = int(self.die_y - temp_h * 1.15)
            self.display_surface.blit(self.instruction_surface, (temp_x, temp_y + 250))

    def display_all_die(self):
        """Displays all die."""
        for x in self.die_object_list:
            x.display_die()

    def display_all_buttons(self):
        """Display all button in list that are active."""
        for x in self.buttons_list:
            if x.active:
                x.display_button()
                x.display_highlighted()

    def display_interface(self):
        """Display all methods that are display related."""
        self.display_surface.blit(self.background_image, (0, 0))
        self.display_points()
        self.display_score()
        self.display_text()
        self.display_all_die()
        self.display_all_buttons()

    def reset_game(self):
        """Resets everything for a new game."""
        self.start_setup()
        self.reset_points(100)
        self.display_interface()
        for i in self.die_object_list:
            i.set_value(1)

    def check_for_lose(self):
        if self.game_rules.points <= 0:
            return True
        else:
            return False