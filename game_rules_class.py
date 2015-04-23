# game_rules_class.py
# Christian Munoz
# 04/10/2015


class GameRules:
    """This class separates the rules of the game."""
    def __init__(self):
        self.list_of_dice = []
        self.points = 100

    def score_dice(self, dice_list):

        counts = [0] * 7
        for i in dice_list:
            counts[i.VALUE] = counts[i.VALUE] + 1

        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 25
        elif (3 in counts) and (2 in counts):
            return "Full House", 15
        elif 3 in counts:
            return "Three of a Kind", 10
        elif not (2 in counts) and (counts[1] == 0 or counts[6] == 0):
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pair", 5
        else:
            return "No Winnings", 0