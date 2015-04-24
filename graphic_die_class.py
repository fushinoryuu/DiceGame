# graphic_die.py
# Christian Munoz
# 03/13/2015

import pygame
import math
from pygame.locals import *
from random import randint

class GraphicDie:
    """class that displays a graphical representation of a 6 sided die"""
    def __init__(self, size, surface, position):
        """This function defines some values of the die and where things should display."""
        self.SURF = surface
        self.POS = position
        self.VALUE = 1
        self.SIZE = size
        self.HOLD = False
        self.ACTIVE = True

        self.DIESURF = pygame.Surface((size, size), flags=SRCALPHA, depth=32)
        self.DIESURF.fill((0, 0, 0, 0))

        # RGB values for later use.
        self.DIEIVORY = (230, 230, 200)
        self.DIERED = (200, 0, 0)
        self.PIPSBLK = (40, 40, 40)
        self.PIPSWHT = (200, 200, 200)
        self.DIECOLORMED = (230, 230, 200)
        self.DIECOLORRED = (200, 0, 0)
        self.DIEDOTSMED = (40, 40, 40)
        self.DIEDOTSLT = (200, 200, 200)

        self.RADIUS = self.SIZE//10
        HSIZE = self.SIZE//2
        QSIZE = self.SIZE//4

        # create Pips/Dots in standard places
        self.POINT1 = (HSIZE, HSIZE)
        self.POINT2 = (QSIZE, QSIZE)
        self.POINT3 = (HSIZE + QSIZE, HSIZE + QSIZE)
        self.POINT4 = (HSIZE + QSIZE, QSIZE)
        self.POINT5 = (QSIZE, HSIZE + QSIZE)
        self.POINT6 = (QSIZE, HSIZE)
        self.POINT7 = (HSIZE + QSIZE, HSIZE)

    def draw_background(self):
        """Create square with rounded corners"""
        if self.HOLD:
            color = self.DIECOLORMED
        else:
            color = self.DIECOLORRED

        pygame.draw.circle(self.DIESURF, color, (self.RADIUS, self.RADIUS), self.RADIUS)
        pygame.draw.circle(self.DIESURF, color, (self.SIZE - self.RADIUS, self.RADIUS), self.RADIUS)
        pygame.draw.circle(self.DIESURF, color, (self.RADIUS, self.SIZE - self.RADIUS), self.RADIUS)
        pygame.draw.circle(self.DIESURF, color, (self.SIZE - self.RADIUS, self.SIZE - self.RADIUS), self.RADIUS)

        pygame.draw.rect(self.DIESURF, color, Rect((self.RADIUS, 0), (self.SIZE - 2 * self.RADIUS, self.SIZE)))
        pygame.draw.rect(self.DIESURF, color, Rect((0, self.RADIUS), (self.SIZE, self.SIZE - 2 * self.RADIUS)))

    def make_pip(self, point):
        """Helper function to make pips."""
        if self.HOLD:
            big_pip = pygame.draw.circle(self.DIESURF, self.DIEDOTSMED, point, self.RADIUS)
        else:
            big_pip = pygame.draw.circle(self.DIESURF, self.DIEDOTSLT, point, self.RADIUS)
        # TODO make more pips
        #medium_pip = pygame.draw.circle(self.DIESURF, self.DIERED, point, (self.RADIUS -2))
        #small_pip = pygame.draw.circle(self.DIESURF, self.PIPSBLK, point, math.ceil(self.RADIUS/2))
        return big_pip  # , pip_medium, pip_small

    def switch_hold(self):
        """Switch the status of the die to the opposite of the current status."""
        self.HOLD = not self.HOLD
        return self.HOLD

    def get_hold(self):
        """Get the current status of the die."""
        return self.HOLD

    def set_hold_true(self):
        """Set the status of the die to True."""
        self.HOLD = True
        return self.HOLD

    def set_hold_false(self):
        """Set the status of the die to False."""
        self.HOLD = False
        return self.HOLD

    def set_active(self):
        """Set the active status as True."""
        self.ACTIVE = True
        return self.ACTIVE

    def set_inactive(self):
        """Set the active status as False."""
        self.ACTIVE = False
        return self.ACTIVE

    def clicked(self, mouse_xy):
        yes_or_no = False
        p1 = self.POS
        p2 = (self.ACTIVE and p1[0] + self.SIZE, p1[1] + self.SIZE)
        yes_or_no = (p1[0] <= mouse_xy[0] <= p2[0] and
                     p1[1] <= mouse_xy[1] <= p2[1])
        return yes_or_no

    def set_random_value(self):
        """Returns a random value between 1-6."""
        self.VALUE = randint(1, 6)
        return self.VALUE

    def draw_value(self, value):
        """Draws the right amount of pips depending on the value of the die."""
        self.draw_background()

        if value == 1:
            pip1 = self.make_pip(self.POINT1)
        elif value == 2:
            pip2 = self.make_pip(self.POINT2)
            pip3 = self.make_pip(self.POINT3)
        elif value == 3:
            pip1 = self.make_pip(self.POINT1)
            pip2 = self.make_pip(self.POINT2)
            pip3 = self.make_pip(self.POINT3)
        elif value == 4:
            pip2 = self.make_pip(self.POINT2)
            pip3 = self.make_pip(self.POINT3)
            pip4 = self.make_pip(self.POINT4)
            pip5 = self.make_pip(self.POINT5)
        elif value == 5:
            pip1 = self.make_pip(self.POINT1)
            pip2 = self.make_pip(self.POINT2)
            pip3 = self.make_pip(self.POINT3)
            pip4 = self.make_pip(self.POINT4)
            pip5 = self.make_pip(self.POINT5)
        elif value == 6:
            pip2 = self.make_pip(self.POINT2)
            pip3 = self.make_pip(self.POINT3)
            pip4 = self.make_pip(self.POINT4)
            pip5 = self.make_pip(self.POINT5)
            pip6 = self.make_pip(self.POINT6)
            pip7 = self.make_pip(self.POINT7)

    def display_die(self):
            self.draw_value(self.VALUE)
            self.SURF.blit(self.DIESURF, self.POS)