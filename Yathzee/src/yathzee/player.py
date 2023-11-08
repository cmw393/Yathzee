from typing import List, Dict
from scoring import Scoring
from dice import YahtzeeDice
from display_dice import display_dice

class Player(Scoring):
    def __init__(self, name=None):
        if name is not None:
            self.name = name
        else:
            self.name = input("Enter player's name: ")
        self.score = 0
        self.turn = self.PlayerTurn(self)
    def is_score_card_full(self):
        # Check if the player's score card contains all categories
        return len(self.score_card()) == len(self.all_categories)
    def get_total_score(self):
        score_card = self.get_score_card()
        total_score = sum(score_card.values())
        return total_score

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
        def choose_category(self):
            print("\nChoose a category for your score:")
            remaining_categories = self.player.score_card.remaining_categories()
        
            for i, category in enumerate(remaining_categories):
                print(f"{i + 1}. {category}")
        
            category_choice = None
            while category_choice is None:
                try:
                    choice = int(input("Enter the number of the category you want to choose: ")) - 1
                    if 0 <= choice < len(remaining_categories):
                        category_choice = remaining_categories[choice]
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Calculate the score for the chosen category and update the score card
            dice_values = self.yahtzee_dice.get_values()
            score = self.player.score_card.calculate_score(category_choice, dice_values)
            print(f"You scored {score} points for {category_choice}!")

        def hold_dice(self, dice_indices):
            self.held_dice.extend(dice_indices)

        def release_dice(self, dice_indices):
            for index in dice_indices:
                self.held_dice.remove(index)    
        def is_turn_over(self):
        # Check if the player's turn is over based on the number of rolls remaining
            return self.rolls_left == 0
        

