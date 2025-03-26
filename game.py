import random

class Game:
    DICE_SYMBOLS = ['⚔️', '🏹', '🛡️', '👑', '🪙', '🪓']

    def __init__(self):
        self.player_hp = 12
        self.enemy_hp = 12

    def get_status(self):
        return{
        "player_hp": self.player_hp,
        "enemy_hp": self.enemy_hp
        }

    def roll_dice(self, num_dice=6):
        return [random.choice(self.DICE_SYMBOLS) for _ in range(num_dice)]
    
    def lose_hp(self, who="player", amount=3):
        if self.player_hp <= 0: return "Verloren"
        if who == "player":
            self.player_hp -= amount
        elif who == "enemy":
            self.enemy_hp -= amount
        return self.end_game()
    
    def add_hp(self, who="player", amount = 5):
        if who == "player": 
            self.player_hp += amount
        elif who == "enemy":
            self.enemy_hp += amount


    def end_game(self):
        if self.player_hp <= 0:
            return "Gegner hat gewonnen!"
        elif self.enemy_hp <= 0:
            return "Du hast gewonnen!"
        else:
            return None  # Spiel läuft noch