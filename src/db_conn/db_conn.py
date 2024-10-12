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
            name TEXT NOT NULL,
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
        ('Blastoise', 90), 
        ('Venusaur', 95), 
        ('Gengar', 100), 
        ('Rayquaza', 120), 
        ('Pikachu', 102);
    ''')

    # Insert Move data
    cursor.execute('''
        INSERT OR IGNORE INTO move (move_name, power, pp)
        VALUES 
        ('Growl', 0, 15), 
        ('Flamethrower', 85, 10), 
        ('Dig', 55, 2), 
        ('Fly', 70, 3);
    ''')

    # Insert Pokémon moves
    cursor.execute('''
        INSERT OR IGNORE INTO pokemon_moves (pokemon_id, move_id)
        VALUES 
        (1, 1),  -- Charizard -> Growl
        (1, 2),  -- Charizard -> Flamethrower
        (1, 3),  -- Charizard -> Dig
        (1, 4);  -- Charizard -> Fly
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
