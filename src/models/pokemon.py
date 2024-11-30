import random
from db_conn.db_conn import get_connection

class Pokemon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @staticmethod
    def get_pokemon_list():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT name, hp FROM pokemon LIMIT 6")
        rows = cursor.fetchall()
        pokemon_list = [Pokemon(name=row[0], hp=row[1]) for row in rows]
        connection.close()
        return pokemon_list

    @staticmethod
    def get_random_computer_pokemon():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT name, hp FROM pokemon ORDER BY pokemon_id DESC LIMIT 6")  # Get the last 3 Pokémon
        rows = cursor.fetchall()
        random_pokemon = random.choice(rows)  # Pick a random Pokémon from the last 6
        connection.close()
        return {'name': random_pokemon[0], 'hp': random_pokemon[1]}

    @staticmethod
    def get_pokemon_by_name(pokemon_name):
        """Fetch a single Pokémon by its name from the database"""
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT name, hp FROM pokemon WHERE name = ?", (pokemon_name,))
        row = cursor.fetchone()
        connection.close()
        if row:
            return Pokemon(name=row[0], hp=row[1])
        else:
            return None

    @staticmethod
    def get_moves_for_pokemon(pokemon_name):
        """Fetch the moves for a specific Pokémon by its name, including move power"""
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT move.move_name, move.pp, move.power
            FROM move
            JOIN pokemon_moves ON move.move_id = pokemon_moves.move_id
            JOIN pokemon ON pokemon.pokemon_id = pokemon_moves.pokemon_id
            WHERE pokemon.name = ?
        """, (pokemon_name,))
        moves = cursor.fetchall()
        connection.close()

        # Return moves including the power of each move
        return [{'move_name': move[0], 'pp': move[1], 'power': move[2]} for move in moves]

