from collections import Counter
from display_dice import score_card
class Scoring:
    def __init__(self):
        self.score_card = {}
        self.all_categories = {
            'Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes',
            'Three-of-a-Kind', 'Four-of-a-Kind', 'Full House',
            'Small Straight', 'Large Straight', 'Yahtzee', 'Chance'
        }

    def calculate_score(self, category, dice_values):
        if category in self.all_categories:
            score = self._calculate_score(category, dice_values)
            self.mark_score(category, score)
            return score
        else:
            raise ValueError(f"Invalid category: {category}")

    def mark_score(self, category, score):
        self.score_card[category] = score

    def get_score_card(self):
        return self.score_card

    def is_category_used(self, category):
        return category in self.score_card

    def _calculate_score(self, category, dice_values):
            if category in {'Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes'}:
                number = int(category[-1])  # Extract the number from the category name
                score = number * dice_values.count(number)
            elif category == 'Three-of-a-Kind':
                counts = Counter(dice_values)
                for value, count in counts.items():
                    if count >= 3:
                        score = sum(dice_values)
                        break
                    else:
                        score = 0
            elif category == 'Four-of-a-Kind':
                counts = Counter(dice_values)
                for value, count in counts.items():
                    if count >= 4:
                        score = sum(dice_values)
                        break
                    else:
                        score = 0
            elif category == 'Full House':
                counts = Counter(dice_values)
                if len(counts) == 2 and 2 in counts.values() and 3 in counts.values():
                    score = sum(dice_values)
                else:
                    score = 0
            elif category == 'Small Straight':
                unique_values = set(dice_values)
                if len(unique_values) >= 4 and (6 in unique_values or (1 in unique_values and 5 in unique_values)):
                    score = 30
                else:
                    score = 0
            elif category == 'Large Straight':
                unique_values = set(dice_values)
                if len(unique_values) == 5 and (max(unique_values) - min(unique_values) == 4):
                    score = 40
                else:
                    score = 0
            elif category == 'Yahtzee':
                counts = Counter(dice_values)
                for value, count in counts.items():
                    if count == 5:
                        score = 50
                        break
                else:
                    score = 0
            elif category == 'Chance':
                score = sum(dice_values)
            else:
                score = 0

            return score

    def remaining_categories(self):
        return list(self.all_categories - set(self.score_card.keys()))

    def num_remaining_categories(self):
        return len(self.remaining_categories())

    def num_used_categories(self):
        return len(self.score_card)
    def is_full(self):
        return self.num_used_categories() == len(self.all_categories)

    def display_score_card(self):
        print("Current Score Card:")
        for category, score in self.get_score_card().items():  # Correct this line
            print(f"{category}: {score}")

        remaining = self.remaining_categories()
        if remaining:
            print("\nRemaining Categories:")
            for category in remaining:
                print(category)
        else:
            print("\nAll categories used.")


