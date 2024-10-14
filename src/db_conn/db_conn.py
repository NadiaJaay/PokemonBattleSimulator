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
        ('Gengar', 80), 
        ('Rayquaza', 110), 
        ('Pikachu', 100);
    ''')

    # Insert Move data
    cursor.execute('''
        INSERT OR IGNORE INTO move (move_name, power, pp)
        VALUES 
        ('Growl', 0, 15), 
        ('Flamethrower', 75, 5), 
        ('Dig', 55, 2), 
        ('Fly', 45, 3),
        ('Dragon Dance', 0, 10),
        ('Outrage', 85, 2),
        ('Earthquake', 80, 1),
        ('Surf', 75, 5),
        ('Ice Beam', 50, 5),
        ('Bite', 30, 10),
        ('Shadow Ball', 50, 3),
        ('Psychic', 90, 1),
        ('Hypnosis', 0, 5),
        ('Razor Leaf', 50, 2),
        ('Sludge Bomb', 0, 5),
        ('Solar Beam', 80, 1),
        ('Thunderbolt', 70, 2),
        ('Quick Attack', 25, 5),
        ('Thunder', 50, 2);
    ''')

    # Insert Pokémon moves
    cursor.execute('''
        INSERT OR IGNORE INTO pokemon_moves (pokemon_id, move_id)
        VALUES 
        (1, 1),  -- Charizard -> Growl
        (1, 2),  -- Charizard -> Flamethrower
        (1, 3),  -- Charizard -> Dig
        (1, 4),  -- Charizard -> Fly
        (5, 5),  -- Rayquaza -> Dragon Dance
        (5, 6),  -- Rayquaza -> Outrage
        (5, 7),  -- Rayquaza -> Earthquake
        (5, 4),  -- Rayquaza -> Fly
        (2, 8),  -- Blastoise -> Surf
        (2, 9),  -- Blastoise -> Ice Beam
        (2, 10),  -- Blastoise -> Bite
        (2, 7),  -- Blastoise -> Earthquake
        (4, 11),  -- Gengar -> Shadow ball
        (4, 12),  -- Gengar -> Psychic
        (4, 13),  -- Gengar -> Hypnosis
        (4, 1),  -- Gengar -> Growl
        (3, 7),  -- Venusaur -> Earthquake
        (3, 14),  -- Venusaur -> Razor Leaf
        (3, 15),  -- Venusaur -> Sludge Bomb
        (3, 16),  -- Venusaur -> Solar Beam
        (6, 17),  -- Pikachu -> Thunderbolt
        (6, 18),  -- Pikachu -> Quick Attack
        (6, 19),  -- Pikachu -> Thunder
        (6, 1);  -- Pikachu -> Growl
        
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
