import random
from dataclasses import dataclass, field
from typing import List

@dataclass
class Dice:
    sides: int = 6
    current_value: int = field(default=None, init=False)

    def roll(self):
        self.current_value = random.randint(1, self.sides)
        return self.current_value

@dataclass
class YahtzeeDice(Dice):
    num_dice: int = 5
    dice_set: List[Dice] = field(default_factory=list)

    def __post_init__(self):
        self.dice_set = [Dice(sides=self.sides) for _ in range(self.num_dice)]

    def roll_all(self):
        return [die.roll() for die in self.dice_set]

    def get_values(self):
        return [die.current_value for die in self.dice_set]
    def get_values(self):
        # Return a list containing the current values of all dice in the set
        values = [die.current_value for die in self.dice_set]
        return values