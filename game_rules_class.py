# game_rules_class.py
# Christian Munoz
# 04/10/2015


class GameRules:
    """This class separates the rules of the game."""
    def __init__(self):
        self.list_of_dice = []
        self.points = 100

    def score_dice(self, dice_list):
        """This function checks the players current hand and scores it according to the rules."""
        counts = [0] * 7
        for i in dice_list:
            counts[i.VALUE] += 1

        #score the hand
        if 7 in counts:
                return "Seven of a Kind", 40
        elif 6 in counts:
            return "Six of a Kind", 35
        elif 5 in counts:
            return "Five of a Kind", 30
        elif (4 in counts) and (3 in counts):
            return "Full House", 25
        elif 4 in counts:
            return "Four of a Kind", 20
        elif counts.count(2) == 3:
            return "Three 2x2 Pairs", 15
        elif not (3 in counts) and (counts[1] == 0 or counts[6] == 0):
            return "Straight", 10
        elif counts.count(3) == 2:
            return "Two 3x3 Pairs", 5
        else:
            return "No Winnings", 0