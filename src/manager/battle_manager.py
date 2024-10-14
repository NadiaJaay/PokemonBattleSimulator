import random
from models.pokemon import Pokemon

class BattleManager:
    def __init__(self, player_pokemon, computer_pokemon):
        self.player_pokemon = player_pokemon
        self.computer_pokemon = computer_pokemon
        self.turn = random.choice(["player", "computer"])  # Randomly choose who starts
        self.winner = None

    def select_random_move(self, pokemon):
        # Filter moves where PP is greater than 0
        valid_moves = [move for move in pokemon.moves if move['pp'] > 0]
        if valid_moves:
            return random.choice(valid_moves)
        return None

    def apply_damage(self, attacking_pokemon, defending_pokemon, move):
        damage = move['power']  # Assuming 'power' is the damage value
        defending_pokemon.hp -= damage
        return defending_pokemon.hp

    def update_move_pp(self, pokemon, move):
        move['pp'] -= 1  # Decrease the PP of the selected move
        return move['pp']

    def check_battle_end(self):
        if self.player_pokemon.hp <= 0:
            self.winner = "computer"
        elif self.computer_pokemon.hp <= 0:
            self.winner = "player"
        return self.winner
