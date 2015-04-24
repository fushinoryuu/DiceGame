# graphic_die_game.py
# Christian Munoz
# 03/13/2015

import pygame
from pygame.locals import *
import sys
from graphic_die_interface import GraphicDieInterface

pygame.init()
game_interface = GraphicDieInterface()

def first_roll():
    game_interface.all_dice_active()
    game_interface.set_value()
    game_interface.b1.highlighted = False
    game_interface.b1.active = False
    game_interface.b2.active = True
    game_interface.instruction_active = True

def second_roll():
    game_interface.set_value()
    game_interface.b2.highlighted = False
    game_interface.b2.active = False
    game_interface.b3.active = True

def third_roll():
    game_interface.set_value()
    game_interface.b3.highlighted = False
    game_interface.b3.active = False
    game_interface.b4.active = True

def final_roll():
    game_interface.set_value()
    game_interface.b4.highlighted = False
    game_interface.b4.active = False
    game_interface.b5.active = True
    game_interface.score_active = True
    game_interface.all_dice_hold()
    game_interface.instruction_active = False
    game_interface.add_points()

def play_again():
    game_interface.all_dice_roll()
    game_interface.set_value()
    game_interface.b5.highlighted = False
    game_interface.b5.active = False
    game_interface.b2.active = True
    game_interface.score_active = False

def main():
    """This function will run the die game."""
    game_interface.start_setup()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                mouse_xy = pygame.mouse.get_pos()

                if game_interface.b1.clicked(mouse_xy):
                    game_interface.b1.highlighted = True
                elif game_interface.b2.clicked(mouse_xy):
                    game_interface.b2.highlighted = True
                elif game_interface.b3.clicked(mouse_xy):
                    game_interface.b3.highlighted = True
                elif game_interface.b4.clicked(mouse_xy):
                    game_interface.b4.highlighted = True
                elif game_interface.b5.clicked(mouse_xy):
                    game_interface.b5.highlighted = True

            if event.type == MOUSEBUTTONUP:
                if game_interface.b1.clicked(mouse_xy):
                    first_roll()
                elif game_interface.die_object_list[0].clicked(mouse_xy):
                    game_interface.die_object_list[0].switch_hold()
                elif game_interface.die_object_list[1].clicked(mouse_xy):
                    game_interface.die_object_list[1].switch_hold()
                elif game_interface.die_object_list[2].clicked(mouse_xy):
                    game_interface.die_object_list[2].switch_hold()
                elif game_interface.die_object_list[3].clicked(mouse_xy):
                    game_interface.die_object_list[3].switch_hold()
                elif game_interface.die_object_list[4].clicked(mouse_xy):
                    game_interface.die_object_list[4].switch_hold()
                elif game_interface.die_object_list[5].clicked(mouse_xy):
                    game_interface.die_object_list[5].switch_hold()
                elif game_interface.die_object_list[6].clicked(mouse_xy):
                    game_interface.die_object_list[6].switch_hold()

                elif game_interface.b2.clicked(mouse_xy):
                    second_roll()
                elif game_interface.b3.clicked(mouse_xy):
                    third_roll()
                elif game_interface.b4.clicked(mouse_xy):
                    final_roll()
                elif game_interface.b5.clicked(mouse_xy):
                    play_again()
        game_interface.display_interface()
        pygame.display.update()

if __name__ == "__main__":
    main()
    sys.exit()
