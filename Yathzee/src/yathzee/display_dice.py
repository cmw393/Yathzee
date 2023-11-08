from typing import List, Dict

def display_dice(values: List[int], held_indices: List[int] = []):
    for index, value in enumerate(values):
        if index in held_indices:
            print(f"[{value}]", end=" ")
        else:
            print(f"{value}", end=" ")
    print()

def score_card(player_name, score_card):
    print(f"Score Card for {player_name}:")
    for category, score in score_card.items():
        print(f"{category}: {score} points")


def display_dice(values: List[int], held_indices: List[int] = []):
    # Define ASCII art for die faces
    dice_faces = {
        1: [
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----"
        ],
        2: [
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----"
        ],
        3: [
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----"
        ],
        4: [
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----"
        ],
        5: [
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----"
        ],
        6: [
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----"
        ]
    }

    # ANSI color codes
    held_color = "\033[92m"  # Green text
    reset_color = "\033[0m"  # Reset to default color

    # Display dice with ASCII art and color coding
    display_lines = [""] * 5
    for row in range(5):
        for index, value in enumerate(values):
            die_face = dice_faces.get(value, [""] * 5)
            if row == 2 and len(die_face) == 5:
                if index in held_indices:
                    display_lines[row] += f"{held_color}{die_face[row]}{reset_color}  "
                else:
                    display_lines[row] += f"{die_face[row]}  "
            else:
                if index in held_indices:
                    display_lines[row] += f"{held_color}{die_face[row]}{reset_color} "
                else:
                    display_lines[row] += f"{die_face[row]} "

    for line in display_lines:
        print(line)

# Example usage:
# display_dice([1, 2, 3, 4, 5], [1, 3])


