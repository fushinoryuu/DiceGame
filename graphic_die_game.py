# graphic_die_game.py
# Christian Munoz
# 03/13/2015

import pygame
import sys
from pygame.locals import *
from graphic_die_interface import GraphicDieInterface

def main():
    """This function will run the die game."""
    pygame.init()

    game_interface = GraphicDieInterface()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        game_interface.display_interface()
        pygame.display.update()

if __name__ == "__main__":
    main()
    sys.exit()
