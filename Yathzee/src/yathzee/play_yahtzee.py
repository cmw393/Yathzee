from player import Player
from display_dice import display_dice

class PlayYahtzee:
    def __init__(self):
        self.player = Player()
        self.game_over_flag = False

    def roll(self):
        self.start_new_turn()
        self.player.display_score_card()
        while not self.player.turn.is_turn_over():
            display_dice(self.player.turn.dice.get_values(), self.player.turn.held_dice)
            self.player.turn.roll()
        self.start_new_turn()

    def choose_category(self):
        self.player.turn.choose_category()

    def start_new_turn(self):
        self.player.turn = self.player.PlayerTurn()

    def turn(self):
        while not self.player.turn.is_turn_over():
            self.roll()
            self.choose_category()



               
    def play_game(self):
        print("Welcome to Yahtzee!")
        while not self.game_over_flag:
            self.turn()
            if self.player.is_score_card_full():
                self.game_over_flag = True
        self.game_over()

    def number_Players(self):
        num_players = int(input("Enter the number of players: "))
        players = [Player() for _ in range(num_players)]

        while True:
            for player in players:
                print(f"{player.name}'s turn:")
                current_turn = player.turn
                current_turn.rolls_left = 3

                while current_turn.rolls_left > 0:
                    current_turn.roll_dice()
                    display_dice(current_turn.get_state())

    def display_dice(self):
        display_dice()


    def game_over(self):
        print("Game Over!")
        self.generate_block_art()
        self.player.display_score_card()
        print("Final Score:", self.player.get_total_score())

if __name__ == "__main__":
    yahtzee = PlayYahtzee()
    yahtzee.play_game()
    yahtzee.number_Players()
    
