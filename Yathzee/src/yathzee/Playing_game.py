import random

class Player:
    def __init__(self, name):
        self.name = name

class YahtzeeGame:
    """
    A Yahtzee game class that allows multiple players to play a single round and displays a scoring board.
    """

    def __init__(self):
        """
        Initialize the YahtzeeGame instance.
        """
        self.players = []
        self.dice = [0, 0, 0, 0, 0]
        self.rolls_remaining = 3
        self.score_sheet = {
            'Aces': None, 'Twos': None, 'Threes': None, 'Fours': None, 'Fives': None, 'Sixes': None,
            'Three-of-a-Kind': None, 'Four-of-a-Kind': None, 'Full House': None,
            'Small Straight': None, 'Large Straight': None, 'Yahtzee': None, 'Chance': None
        }
        self.available_categories = set(self.score_sheet.keys())
        self.upper_section = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
        self.bonus_threshold = 63
        self.bonus_score = 35

    def get_num_players(self):
        """
        Ask the user for the number of players.

        Returns:
            int: The number of players.
        """
        while True:
            try:
                num_players = int(input("Enter the number of players: "))
                if num_players > 0:
                    return num_players
                else:
                    print("Please enter a valid number of players.")
            except ValueError:
                print("Please enter a valid number.")

    def get_player_names(self, num_players):
        """
        Collect the names of players and store them in the `players` list.

        Args:
            num_players (int): The number of players.
        """
        for i in range(num_players):
            name = input(f"Enter the name of player {i + 1}: ")
            player = Player(name)
            self.players.append(player)

    def __init__(self):
        """
        Initialize the YahtzeeGame instance.
        """
        self.dice = [0, 0, 0, 0, 0]
        self.rolls_remaining = 3
        self.score_sheet = {
            'Aces': None, 'Twos': None, 'Threes': None, 'Fours': None, 'Fives': None, 'Sixes': None,
            'Three-of-a-Kind': None, 'Four-of-a-Kind': None, 'Full House': None,
            'Small Straight': None, 'Large Straight': None, 'Yahtzee': None, 'Chance': None
        }
        self.available_categories = set(self.score_sheet.keys())
        self.upper_section = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
        self.bonus_threshold = 63
        self.bonus_score = 35

    def roll_dice(self):
        """
        Roll five dice.
        """
        self.dice = [random.randint(1, 6) for _ in range(5)]

    def re_roll(self, dice_to_reroll):
        """
        Reroll selected dice.

        Args:
            dice_to_reroll (list): List of indices of dice to reroll.
        """
        for index in dice_to_reroll:
            self.dice[index] = random.randint(1, 6)

    def display_dice(self):
        """
        Display the current state of the dice.
        """
        print("Current dice:", self.dice)

    def choose_category(self):
        """
        Allow the player to choose a category to score.
        """
        while True:
            print("Available categories:", self.available_categories)
            try:
                category = input("Choose a category: ")
                if category in self.available_categories:
                    return category
                else:
                    print("Category already used or invalid.")
            except ValueError:
                print("Invalid input. Please enter a valid category name.")

    def play_turn(self):
        """
        Play a single turn of Yahtzee, including rolling, rerolling, and scoring.
        """
        while self.rolls_remaining > 0:
            self.roll_dice()
            self.display_dice()

            if self.rolls_remaining > 1:
                reroll_choice = input("Do you want to reroll some dice? (y/n): ")
                if reroll_choice.lower() == 'y':
                    reroll_indices = [int(x) for x in input("Enter the indices of dice to reroll (0-4): ").split()]
                    self.re_roll(reroll_indices)
                    self.display_dice()
                else:
                    break
            else:
                break

            self.rolls_remaining -= 1

        category = self.choose_category()
        score = self.calculate_score(category)
        self.score_sheet[category] = score
        self.available_categories.remove(category)
        self.display_score_board()

    def calculate_score(self, category):
        """
        Calculate the score for a given category.

        Args:
            category (str): The category name.

        Returns:
            int: The score for the chosen category.
        """
        if category in self.upper_section:
            return self.dice.count(self.upper_section.index(category) + 1) * (self.upper_section.index(category) + 1)
        elif category == 'Three-of-a-Kind':
            for die in set(self.dice):
                if self.dice.count(die) >= 3:
                    return sum(self.dice)
            return 0
        elif category == 'Four-of-a-Kind':
            for die in set(self.dice):
                if self.dice.count(die) >= 4:
                    return sum(self.dice)
            return 0
        elif category == 'Full House':
            counts = [self.dice.count(die) for die in set(self.dice)]
            if 2 in counts and 3 in counts:
                return 25
            return 0
        elif category == 'Small Straight':
            dice_set = set(self.dice)
            if len(dice_set) >= 4:
                for i in range(1, 4):
                    if i not in dice_set:
                        return 0
                return 30
            return 0
        elif category == 'Large Straight':
            dice_set = set(self.dice)
            if len(dice_set) == 5 and max(dice_set) - min(dice_set) == 4:
                return 40
            return 0
        elif category == 'Yahtzee':
            if self.dice.count(self.dice[0]) == 5:
                return 50
            return 0
        elif category == 'Chance':
            return sum(self.dice)
        else:
            return 0

    def display_score_board(self):
     """
     Display the current score board.
     """
     print("Current Score Board:")
     for category, score in self.score_sheet.items():
         if score is not None:
            print(f"{category}: {score}")
         else:
            print(f"{category}: -")
    
     # Calculate the total score based on non-None scores
     total_score = sum(score for score in self.score_sheet.values() if score is not None)
    
     if total_score >= self.bonus_threshold:
        total_score += self.bonus_score
     print(f"Total Score: {total_score}")


    def play_game(self):
        """
        Play a complete game of Yahtzee.
        """
        print("Welcome to Yahtzee!")

        while self.rolls_remaining > 0 and self.available_categories:
            print(f"Remaining rolls: {self.rolls_remaining}, Remaining categories: {self.available_categories}")
            self.play_turn()

        print("Game over!")
        self.display_score_board()

if __name__ == "__main__":
    yahtzee = YahtzeeGame()
    num_players = yahtzee.get_num_players()
    yahtzee.get_player_names(num_players)
    yahtzee.play_game()

if __name__ == "__main__":
    yahtzee = YahtzeeGame()
    yahtzee.play_game()


