import sqlite3

#connect to the database
conn = sqlite3.connect("../../pokemonDetails.db")

#create cursor object
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE pokemon (
            pokemon_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hp INTEGER NOT NULL

)""")

cursor.execute("""
    CREATE TABLE move (
            move_id INTEGER PRIMARY KEY AUTOINCREMENT,
            move_name TEXT NOT NULL,
            power INTEGER NOT NULL,
            pp INTEGER NOT NULL

)""")

cursor.execute("""
    CREATE TABLE battle_summary (
            battle_id_id INTEGER PRIMARY KEY AUTOINCREMENT,
            pokemon_id INTEGER NOT NULL,
            move_id INTEGER NOT NULL,
            damage_dealt INTEGER NOT NULL,
            turn INTEGER NOT NULL,
            FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
            FOREIGN KEY (move_id) REFERENCES move(move_id)

)""")

cursor.execute("""
    CREATE TABLE pokemon_moves (
            pokemon_id INTEGER NOT NULL,
            move_id INTEGER NOT NULL,
            PRIMARY KEY (pokemon_id, move_id),
            FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
            FOREIGN KEY (move_id) REFERENCES move(move_id)

)""")

cursor.execute('''
    INSERT INTO pokemon (name, hp) 
    VALUES ('Charizard', 100), ('Blastoise', 90), ('Venusaur', 95), ('Gengar', 100), ('Rayquaza', 120), ('Pikachu', 102);
''')

cursor.execute('''
    INSERT INTO move (move_name, power, pp)
    VALUES ('Growl', 0, 15), ('Flamethrower', 85, 10), ('Dig', 55, 2), ('Fly', 70, 3);
''')

cursor.execute('''
    INSERT INTO pokemon_moves (pokemon_id, move_id)
    VALUES 
    (1, 1),  -- Charizard -> Growl
    (1, 2),  -- Charizard -> Flamethrower
    (1, 3),  -- Charizard -> Dig
    (1, 4);  -- Charizard -> Fly
''')

cursor.execute('''
    SELECT move.move_name
    FROM move
    JOIN pokemon_moves ON move.move_id = pokemon_moves.move_id
    JOIN pokemon ON pokemon.pokemon_id = pokemon_moves.pokemon_id
    WHERE pokemon.name = 'Charizard';
''')

moves = cursor.fetchall()
for move in moves:
    print(move[0])

conn.commit()

#commit transaction
conn.commit()

conn.close()
print("Tables created succesfully")