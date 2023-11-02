from typing import List, Dict
from scoring import Scoring
from dice import YahtzeeDice
from display_dice import display_dice

class Player(Scoring):
    def __init__(self):
        self.name = input("Enter player's name: ")
        self.score = 0
        self.turn = self.PlayerTurn(self)

    class PlayerTurn:
        def __init__(self, player):
            self.player = player
            self.yahtzee_dice = YahtzeeDice()
            self.rolls_left = 3
            self.held_dice = []

        def get_state(self):
            return {
                "dice_values": self.yahtzee_dice.get_values(),
                "rolls_left": self.rolls_left,
                "held_dice": self.held_dice
            }

        def roll_dice(self):
            if self.rolls_left == 0:
                return False

            dice_indices_to_roll = [i for i in range(len(self.yahtzee_dice.dice_set)) if i not in self.held_dice]
            self.yahtzee_dice.roll(dice_indices_to_roll)
            self.rolls_left -= 1
            return True

        def hold_dice(self, dice_indices):
            self.held_dice.extend(dice_indices)

        def release_dice(self, dice_indices):
            for index in dice_indices:
                self.held_dice.remove(index)

