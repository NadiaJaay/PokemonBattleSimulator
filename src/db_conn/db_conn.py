import sqlite3

# Function to get the database connection
def get_connection():
    connection = sqlite3.connect("../../pokemonDetails.db")
    return connection

# Function to create the tables if they do not exist
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Create the tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            pokemon_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE, 
            hp INTEGER NOT NULL
        );
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS move (
            move_id INTEGER PRIMARY KEY AUTOINCREMENT,
            move_name TEXT NOT NULL,
            power INTEGER NOT NULL,
            pp INTEGER NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_moves (
            pokemon_id INTEGER NOT NULL,
            move_id INTEGER NOT NULL,
            PRIMARY KEY (pokemon_id, move_id),
            FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
            FOREIGN KEY (move_id) REFERENCES move(move_id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS battle_summary (
            battle_id INTEGER PRIMARY KEY AUTOINCREMENT,
            pokemon_id INTEGER NOT NULL,
            move_id INTEGER NOT NULL,
            damage_dealt INTEGER NOT NULL,
            turn INTEGER NOT NULL,
            FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
            FOREIGN KEY (move_id) REFERENCES move(move_id)
        );
    """)

    conn.commit()
    conn.close()

# Function to insert initial data
def insert_initial_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert Pokemon data
    cursor.execute('''
        INSERT OR IGNORE INTO pokemon (name, hp) 
        VALUES 
        ('Charizard', 100), 
        ('Blastoise', 100), 
        ('Venusaur', 100), 
        ('Raichu', 100), 
        ('Groudon', 100), 
        ('Nidoqueen', 100), 
        ('Gengar', 100), 
        ('Rayquaza', 110), 
        ('Mewtwo', 110), 
        ('Giratina', 110), 
        ('Lapras', 110), 
        ('Pikachu', 100);
    ''')

    # Insert Move data
    cursor.execute('''
        INSERT OR IGNORE INTO move (move_name, power, pp)
        VALUES 
        ('Growl', 0, 5), 
        ('Flamethrower', 65, 5), 
        ('Dig', 35, 2), 
        ('Fly', 25, 3),
        ('Dragon Dance', 0, 5),
        ('Outrage', 70, 2),
        ('Earthquake', 80, 1),
        ('Surf', 50, 5),
        ('Ice Beam', 20, 5),
        ('Bite', 30, 10),
        ('Shadow Ball', 50, 3),
        ('Psychic', 70, 1),
        ('Hypnosis', 0, 5),
        ('Razor Leaf', 40, 2),
        ('Sludge Bomb', 0, 3),
        ('Solar Beam', 33, 1),
        ('Thunderbolt', 40, 2),
        ('Quick Attack', 25, 5),
        ('Thunder', 50, 2),
        ('Mud Shot', 25, 2), -- 20
        ('Calm Mind', 0, 3);
    ''')

    # Insert Pokémon moves
    cursor.execute('''
        INSERT OR IGNORE INTO pokemon_moves (pokemon_id, move_id)
        VALUES 
        (1, 1),  -- Charizard -> Growl
        (1, 2),  -- Charizard -> Flamethrower
        (1, 3),  -- Charizard -> Dig
        (1, 4),  -- Charizard -> Fly
        (8, 5),  -- Rayquaza -> Dragon Dance
        (8, 6),  -- Rayquaza -> Outrage
        (8, 7),  -- Rayquaza -> Earthquake
        (8, 4),  -- Rayquaza -> Fly
        (2, 8),  -- Blastoise -> Surf
        (2, 9),  -- Blastoise -> Ice Beam
        (2, 10),  -- Blastoise -> Bite
        (2, 7),  -- Blastoise -> Earthquake
        (7, 11),  -- Gengar -> Shadow ball
        (7, 12),  -- Gengar -> Psychic
        (7, 13),  -- Gengar -> Hypnosis
        (7, 1),  -- Gengar -> Growl
        (3, 7),  -- Venusaur -> Earthquake
        (3, 14),  -- Venusaur -> Razor Leaf
        (3, 15),  -- Venusaur -> Sludge Bomb
        (3, 16),  -- Venusaur -> Solar Beam
        (12, 17),  -- Pikachu -> Thunderbolt
        (12, 18),  -- Pikachu -> Quick Attack
        (12, 19),  -- Pikachu -> Thunder
        (12, 1),  -- Pikachu -> Growl
        (4, 1),  -- Raichu -> Growl
        (4, 2),  -- Raichu -> Flamethrower
        (4, 3),  -- Raichu -> Dig
        (4, 4),  -- Raichu -> Fly
        (5, 16),  -- Groudon -> Solar Beam
        (5, 2),  -- Groudon -> Flamethrower
        (5, 7),  -- Groudon -> Earthquake
        (5, 20),  -- Groudon -> Mud Shot
        (6, 15),  -- Nidoqueen -> Sludge Bomb
        (6, 11),  -- Nidoqueen -> Shadow ball
        (6, 10),  -- Nidoqueen -> Bite
        (6, 7),  -- Nidoqueen -> Earthquake
        (9, 17),  -- Mewtwo -> Thunderbolt
        (9, 12),  -- Mewtwo -> Psychic
        (9, 21),  -- Mewtwo -> Calm Mind
        (9, 9),  -- Mewtwo -> Ice Beam
        (10, 7),  -- Giratina -> Earthquake
        (10, 11),  -- Giratina -> shadow ball
        (10, 13),  -- Giratina -> Hypnosis
        (10, 6),  -- Giratina -> Outrage
        (11, 8),  -- Lapras -> Surf
        (11, 18),  -- Lapras -> Quick Attack
        (11, 19),  -- Lapras -> Thunder
        (11, 9);  -- Lapras -> Ice Beam
  
    ''')

    conn.commit()
    conn.close()

# Initialize the database (create tables and insert data)
def initialize_db():
    create_tables()
    insert_initial_data()
    print("Database initialized successfully")

# Call initialize_db to ensure tables and data are created
initialize_db()
