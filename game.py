import random

class Game:
    DICE_SYMBOLS = ['⚔️', '🏹', '🛡️', '👑', '🪙', '🪓']

    def __init__(self):
        self.player_hp = 15

    def roll_dice(self, num_dice=6):
        return [random.choice(self.DICE_SYMBOLS) for _ in range(num_dice)]
