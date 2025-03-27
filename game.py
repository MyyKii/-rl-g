import random

class Game:
    DICE_SYMBOLS = ['⚔️', '🏹', '🛡️', '👑', '🪙', '🪓']

    def __init__(self):
        self.player_1_hp = 12
        self.player_2_hp = 12
        self.active_player = random.randint(1,2)
        self.game_terminated = False

    def get_status(self):
        return{
        "player_1_hp": self.player_1_hp,
        "player_2_hp": self.player_2_hp,
        #"turn": self.active_player
        }

    def roll_dice(self, num_dice=6):
        return [random.choice(self.DICE_SYMBOLS) for _ in range(num_dice)]

    def add_hp(self, who="player_1", amount = 5):
        if who == "player_1": 
            self.player_1_hp += amount
        elif who == "player_2":
            self.player_2_hp += amount

    def lose_hp(self, who):
        damage = random.randint(1, 5)
        if who == "player_1":
            self.player_1_hp = max(self.player_1_hp - damage, 0)
        else:
            self.player_2_hp = max(self.player_2_hp - damage, 0)
        return self.end_game()

    def player_1_turn(self):
        if self.active_player == 1 and not self.game_terminated:
            result = self.lose_hp("player_2")
            self.active_player = 2
            return result

    def player_2_turn(self):
        if self.active_player == 2 and not self.game_terminated:
            result = self.lose_hp("player_1")
            self.active_player = 1
            return result

    def end_game(self):
        if self.player_1_hp <= 0:
            self.game_terminated = True
            return "Spieler 2 hat gewonnen!"
        elif self.player_2_hp <= 0:
            self.game_terminated = True
            return "Spieler 1 hast gewonnen!"
        return None
