from player import Player
from display_dice import display_dice
class PlayYahtzee:
    def __init__(self):
        player_name = input("Enter your name: ")  # Get the player's name from user input
        self.player = Player(player_name)  # Create a Player instance with the player's name
        self.game_over_flag = False

    def roll(self):
        self.start_new_turn()
        self.player.display_score_card()
        while not self.player.turn.is_turn_over():
            display_dice(self.player.turn.yahtzee_dice.get_values(), self.player.turn.held_dice)
            self.player.turn.roll_dice()
        self.start_new_turn()

    def choose_category(self):
        self.player.turn.choose_category()

    def start_new_turn(self):
        self.player.turn = self.player.PlayerTurn(self)


    def turn(self):
        while not self.player.turn.is_turn_over():
            self.roll()
            self.choose_category()

    def play_game(self):
        print("Welcome to Yahtzee!")
        while not self.game_over_flag:
            self.turn.turn()  # Corrected method call
            if self.player.is_score_card_full():
                self.game_over_flag = True
        self.game_over()


    def display_dice(self, values, held_indices):
        display_dice(values, held_indices)

    def game_over(self):
        print("Game Over!")
        self.display_dice(self.player.turn.yahtzee_dice.get_values(), self.player.turn.held_dice)
        self.player.display_score_card()
        print("Final Score:", self.player.get_total_score())

if __name__ == "__main__":
    yahtzee = PlayYahtzee()
    yahtzee.play_game()

    
