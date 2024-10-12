# models/pokemon.py
from db_conn.db_conn import get_connection

class Pokemon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @staticmethod
    def get_pokemon_list(limit=3):
        """Retrieve the first `limit` Pokémon from the database."""
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT name, hp FROM pokemon LIMIT ?", (limit,))
        rows = cursor.fetchall()
        connection.close()
        return [Pokemon(name=row[0], hp=row[1]) for row in rows]

