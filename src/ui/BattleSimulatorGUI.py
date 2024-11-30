from tkinter import *
from tkinter import messagebox
from models.pokemon import Pokemon  # Import the Pokemon model

import pygame
import random
import os

# Get the base directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "../images")

# window config
window = Tk()
window.geometry("700x500")
window.title("PokemonBattleSimulator")
window.config(background="#FFDD57")

pygame.mixer.init()

def play_music():
    pygame.mixer.music.load(os.path.join(BASE_DIR, "../sfx/10 Relic Song.mp3"))
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()

def toggle_music():
    if pygame.mixer.music.get_busy():
        stop_music()
    else:
        play_music()

play_music()

# Global variables for battle state
player_pokemon = None
computer_pokemon = None
turn = None
battle_log = None
computer_label = None
player_label = None
move_buttons = []
moves = []
turn_count = 0

# Function to handle Pokémon selection
def select_pokemon(pokemon_name):
    # Clear current screen
    for widget in window.winfo_children():
        widget.destroy()

    start_battle_screen(pokemon_name)

# Function to start the battle and show player vs computer Pokémon
def start_battle_screen(player_pokemon_name):
    global player_pokemon, computer_pokemon, turn, battle_log, computer_label, player_label, move_buttons, moves

    # Clear current screen
    for widget in window.winfo_children():
        widget.destroy()

    # Get computer's random Pokémon
    computer_pokemon = Pokemon.get_random_computer_pokemon()
    computer_pokemon['moves'] = Pokemon.get_moves_for_pokemon(computer_pokemon['name'])

# Player's Pokémon (fetch the selected Pokémon details from the DB)
    player_pokemon = Pokemon.get_pokemon_by_name(player_pokemon_name)

    # Randomly choose who goes first (0 for player, 1 for computer)
    turn = random.choice([0, 1])

    # Mapping of Pokémon names to their image paths using dynamic paths
    pokemon_images = {
        "Pikachu": os.path.join(IMAGE_DIR, "pikachu.png"),
        "Rayquaza": os.path.join(IMAGE_DIR, "rayquaza.png"),
        "Gengar": os.path.join(IMAGE_DIR, "gengar.png"),
        "Mewtwo": os.path.join(IMAGE_DIR, "Mewtwo.png"),
        "Lapras": os.path.join(IMAGE_DIR, "Lapras.png"),
        "Giratina": os.path.join(IMAGE_DIR, "Giratina.png"),
        "Charizard": {
            "back": os.path.join(IMAGE_DIR, "charizard_back.png")
        },
        "Blastoise": {
            "back": os.path.join(IMAGE_DIR, "blastoise_back.png")
        },
        "Venusaur": {
            "back": os.path.join(IMAGE_DIR, "venusaur_back.png")
        },
        "Groudon": {
            "back": os.path.join(IMAGE_DIR, "groudon_back.png")
        },
        "Raichu": {
            "back": os.path.join(IMAGE_DIR, "raichu_back.png")
        },
        "Nidoqueen": {
            "back": os.path.join(IMAGE_DIR, "nidoqueen_back.png")
        }
    }

    # Top-left: Computer Pokémon
    computer_label = Label(window, text=f"{computer_pokemon['name']}\nHP: {computer_pokemon['hp']}",
                           font=('Arial', 15), bg="white", fg="black", width=15)
    computer_label.place(x=10, y=50)

    # Display computer's Pokémon image
    if computer_pokemon['name'] in pokemon_images:
        opponent_image_path = pokemon_images[computer_pokemon['name']]
        opponent_image = PhotoImage(file=opponent_image_path).subsample(9, 9)
        opponent_image_label = Label(window, image=opponent_image, bg="#FFDD57")
        opponent_image_label.image = opponent_image
        opponent_image_label.place(x=480, y=100)

    # Display player's Pokémon back image
    if player_pokemon.name in pokemon_images:
        player_image_path = pokemon_images[player_pokemon.name]["back"]
        player_image = PhotoImage(file=player_image_path).zoom(2, 2)
        player_image_label = Label(window, image=player_image, bg="#FFDD57")
        player_image_label.image = player_image
        player_image_label.place(x=80, y=200)

    # Right-bottom: Player's Pokémon and moves
    player_label = Label(window, text=f"{player_pokemon.name}\nHP: {player_pokemon.hp}",
                         font=('Arial', 15), bg="white", fg="black", width=15)
    player_label.place(x=550, y=310)  # Position at the bottom-right

    # Battle log
    battle_log = Label(window, text=f"{computer_pokemon['name']} appeared! Prepare for battle!",
                       font=('Arial', 14), bg="#FFDD57", fg="black")
    battle_log.pack(pady=20)

    # Moves section
    move_section = Frame(window, bg="#FFDD57")
    move_section.pack(side=BOTTOM, pady=20)

    action_label = Label(window, text=f"What will {player_pokemon.name} do?", font=('Arial', 14), bg="#FFDD57", fg="black")
    action_label.place(x=50, y=400)

    # Moves buttons
    moves = Pokemon.get_moves_for_pokemon(player_pokemon_name)
    move_buttons = []  # Reset the move buttons list

    # Add move buttons dynamically
    for idx, move in enumerate(moves):
        move['max_pp'] = move['pp']  # Store the maximum PP
        move_button = Button(move_section, text=f"{move['move_name']}\nPP: {move['pp']}/{move['max_pp']}",
                             font=('Arial', 12), padx=10, pady=5, bg="white", fg="black", width=10,
                             command=lambda i=idx: player_move(i))
        move_button.grid(row=(1 + idx // 2), column=(1 + idx % 2), padx=10, pady=5)
        move_buttons.append(move_button)

    # Check if it's the computer's turn to start the battle
    if turn == 1:
        computer_move()

def player_move(move_index):
    global computer_pokemon
    global computer_pokemon, turn_count
    turn_count += 1  # Increment turn count each time a move is made
    move = moves[move_index]

    # Check if the move still has PP
    if move['pp'] == 0:
        update_battle_log(f"{player_pokemon.name}'s {move['move_name']} has no PP left! Please select a different move.")
        return  # Don't allow the move if PP is zero

    # Deduct one PP for the move
    move['pp'] -= 1
    update_move_buttons()  # Update PP on the move buttons

    # Calculate damage using the move's power
    damage = move.get('power', 0)  # Default to 0 if no power is provided
    computer_pokemon['hp'] -= damage  # Reduce computer's Pokémon HP
    computer_pokemon['hp'] = max(0, computer_pokemon['hp'])
    # Log the player's move in the battle log
    update_battle_log(f"{player_pokemon.name} used {move['move_name']}! It dealt {damage} damage!" if damage > 0 else f"{player_pokemon.name} used {move['move_name']}! It did no damage.")

    # Update the HP labels in the UI
    update_hp_labels()

    window.after(1000, check_computer_fainted)

def update_move_buttons():
    for idx, move in enumerate(moves):
        button_text = f"{move['move_name']}\nPP: {move['pp']}/{move['max_pp']}"
        move_buttons[idx].config(text=button_text)

        # Disable the button if PP is zero
        if move['pp'] == 0:
            move_buttons[idx].config(state=DISABLED)

# Function to check if computer's Pokémon fainted
def check_computer_fainted():
    if computer_pokemon['hp'] <= 0:
        update_battle_log(f"{computer_pokemon['name']} fainted! You win!")
        window.after(2000, lambda: go_to_battle_summary("You Won"))

    else:
        disable_move_buttons()
        window.after(2000, computer_move) #added delay between player and computers turns
        #computer_move()

def computer_move():
    global player_pokemon

    # Use the tracked moves in the `computer_pokemon` object
    moves = computer_pokemon['moves']

    # Filter moves to only include those with PP > 0
    available_moves = [move for move in moves if move['pp'] > 0]

    # Check if there are any valid moves left
    if not available_moves:
        update_battle_log(f"{computer_pokemon['name']} has no moves left! It skips its turn.")
        enable_move_buttons()  # Re-enable the player's move buttons
        return

    # Randomly select a move from the available moves
    move = random.choice(available_moves)

    # Deduct one PP from the selected move
    move['pp'] -= 1

    # Calculate damage and reduce player's Pokémon HP
    damage = move.get('power', 0)
    player_pokemon.hp -= damage
    player_pokemon.hp = max(0, player_pokemon.hp)  # Ensure HP doesn't drop below 0

    # Log the computer's move
    update_battle_log(f"{computer_pokemon['name']} used {move['move_name']}! It dealt {damage} damage!" if damage > 0 else f"{computer_pokemon['name']} used {move['move_name']}! It did no damage.")

    # Update HP labels on the screen
    update_hp_labels()

    # Delay before checking if the player's Pokémon has fainted
    window.after(2000, check_player_fainted)

# Function to check if player's Pokémon fainted
def check_player_fainted():
    if player_pokemon.hp <= 0:
        update_battle_log(f"{player_pokemon.name} fainted! You lose!")
        window.after(2000, lambda: go_to_battle_summary("You Lost"))

    else:
        enable_move_buttons()

def disable_move_buttons():
    for button in move_buttons:
        button.config(state=DISABLED)

def enable_move_buttons():
    for button in move_buttons:
        button.config(state=NORMAL)

# Function to go to the Battle Summary page
def go_to_battle_summary(outcome):
    global turn_count

    # Clear current screen
    for widget in window.winfo_children():
        widget.destroy()

    # Create a white frame for the summary box
    summary_frame = Frame(window, bg="white", bd=2, relief="solid", padx=100, pady=20, width=600)
    summary_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Add the battle summary details inside the frame
    label = Label(summary_frame, text="Battle Summary", font=("Arial", 30, "bold"), bg="white", fg="black")
    label.pack(pady=10)

    outcome_label = Label(summary_frame, text=f"Outcome: {outcome}", font=("Arial", 20), bg="white", fg="black")
    outcome_label.pack(pady=5)

    player_label = Label(summary_frame, text=f"Player's Pokémon: {player_pokemon.name}", font=("Arial", 20), bg="white", fg="black")
    player_label.pack(pady=5)

    computer_label = Label(summary_frame, text=f"Computer's Pokémon: {computer_pokemon['name']}", font=("Arial", 20), bg="white", fg="black")
    computer_label.pack(pady=5)

    turns_label = Label(summary_frame, text=f"Turns Taken: {turn_count}", font=("Arial", 20), bg="white", fg="black")
    turns_label.pack(pady=5)

    # Add a Home button inside the frame
    home_button = Button(summary_frame, text="Home", font=("Arial", 15), command=show_play_screen, bg="#FFDD57", fg="black", width=10)
    home_button.pack(pady=20)

# Function to update the battle log with messages
def update_battle_log(message):

    # Create a frame for the battle log with a white background
    battle_frame = Frame(window, bg="white", padx=10, pady=10)
    battle_frame.place(x=30, y=320, width=500)

    # Update the battle log message inside the frame
    battle_log = Label(battle_frame, text=message, font=('Arial', 14), bg="white", fg="black", wraplength=800)
    battle_log.pack()

# Function to update HP labels on the screen
def update_hp_labels():
    computer_label.config(text=f"{computer_pokemon['name']}\nHP: {computer_pokemon['hp']}")
    player_label.config(text=f"{player_pokemon.name}\nHP: {player_pokemon.hp}")

# Function to start the battle and show Pokémon selection buttons
def start_battle():
    global player_pokemon, computer_pokemon, turn, battle_log, computer_label, player_label, move_buttons, moves, turn_count
    turn_count = 0
    # Clear current screen
    for widget in window.winfo_children():
        widget.destroy()

    # Fetch Pokémon from the database using the model
    pokemon_options = Pokemon.get_pokemon_list()

    label = Label(window, text="Select a Pokémon...", font=("Ariel", 40), bg="#FFDD57", fg="black")
    label.pack(side=BOTTOM, padx=70, pady=100)

    # Mapping Pokémon names to their images and subsample values
    pokemon_images = {
        "Charizard": (os.path.join(IMAGE_DIR, "charizard.png"), 7),
        "Blastoise": (os.path.join(IMAGE_DIR, "blastoise.png"), 10),
        "Venusaur": (os.path.join(IMAGE_DIR, "venusaur.png"), 10),
        "Raichu": (os.path.join(IMAGE_DIR, "raichu.png"), 8),
        "Groudon": (os.path.join(IMAGE_DIR, "groudon.png"), 10),
        "Nidoqueen": (os.path.join(IMAGE_DIR, "nidoqueen.png"), 9)
    }

    # Create a frame for the Pokémon selection grid
    pokemon_frame = Frame(window, bg="#FFDD57")
    pokemon_frame.pack()

    # Add Pokémon image buttons in a 2-row layout (3 per row)
    for idx, pokemon in enumerate(pokemon_options):
        if pokemon.name in pokemon_images:
            image_path, subsample_value = pokemon_images[pokemon.name]
            pokemon_image = PhotoImage(file=image_path).subsample(subsample_value, subsample_value)
            pokemon_button = Button(pokemon_frame, image=pokemon_image, bg="#FFDD57", command=lambda p=pokemon.name: select_pokemon(p))
            pokemon_button.image = pokemon_image  # Keep a reference to avoid garbage collection
            pokemon_button.grid(row=idx // 3, column=idx % 3, padx=20, pady=10)

# Function to show the play screen after agreeing to the disclaimer
def show_play_screen():
    # Clear current screen
    for widget in window.winfo_children():
        widget.destroy()

    logo_image_play = PhotoImage(file=os.path.join(IMAGE_DIR, "PokemonLogo.png"))
    logo_label_play = Label(window, image=logo_image_play, bg="#FFDD57")
    logo_label_play.image = logo_image_play
    logo_label_play.pack()

    battle_img = PhotoImage(file=os.path.join(IMAGE_DIR, "BattleImg.png"))
    battle_img_label = Label(window, image=battle_img, bg="#FFDD57")
    battle_img_label.image = battle_img
    battle_img_label.pack()

    pokemon_image_play = PhotoImage(file=os.path.join(IMAGE_DIR, "umbreon.png")).subsample(5, 5)
    pokemon_label_play = Label(window, image=pokemon_image_play, bg="#FFDD57")
    pokemon_label_play.image = pokemon_image_play
    pokemon_label_play.pack()

    settings_img = PhotoImage(file=os.path.join(IMAGE_DIR, "settings.png")).subsample(35, 35)
    settings_button = Button(window, image=settings_img, command=show_settings_page, bg="#FFDD57", borderwidth=0, highlightthickness=0)
    settings_button.image = settings_img
    settings_button.pack(side=RIGHT, padx=10)

    # Create Play Screen with a Play Button

    sound_img = PhotoImage(file=os.path.join(IMAGE_DIR, "sound.png")).subsample(20, 20)
    sound_button = Button(window, image=sound_img, command=toggle_music, bg="#FFDD57", borderwidth=0, highlightthickness=0)
    sound_button.image = sound_img
    sound_button.pack(side=LEFT, padx=10)

    play_button = Button(window, text="PLAY", font=('Arial', 20), command=start_battle)
    play_button.pack()

# ---------------------
# Load logo and disclaimer
logo_path = os.path.join(IMAGE_DIR, "PokemonLogo.png")
logo_image = PhotoImage(file=logo_path)
logo_label = Label(window, image=logo_image, bg="#FFDD57")
logo_label.pack()

battle_img_path = os.path.join(IMAGE_DIR, "BattleImg.png")
battle_img = PhotoImage(file=battle_img_path)
battle_img_label = Label(window, image=battle_img, bg="#FFDD57")
battle_img_label.pack()

# Create Disclaimer Frame (for the border)
disclaimer_frame = Frame(window, bd=2, relief="solid", padx=10, pady=10, bg="black")
disclaimer_frame.pack(pady=20)

disclaimer_label = Label(disclaimer_frame, text="DISCLAIMER", font=('Arial', 30, 'bold'), bg="black", fg="white")
disclaimer_label.pack()

disclaimer_text = Label(disclaimer_frame, text="This Pokémon Battle Simulator is a fan-made project and is not affiliated with or endorsed by Nintendo, Game Freak, or The Pokémon Company. All Pokémon characters and related assets are the property of their respective owners. This simulator is created purely for entertainment purposes and is free to use. No copyright infringement is intended.", wraplength=400, bg="black", fg="white")
disclaimer_text.pack()

agree_button = Button(disclaimer_frame, text="AGREE", font=('Arial', 15), command=show_play_screen)
agree_button.pack(pady=20)

# ---------------------
def show_settings_page():
    # Clear current screen
    for widget in window.winfo_children():
        widget.destroy()

    label = Label(window, text="Select Window Size", font=("Arial", 20), bg="#FFDD57", fg="black")
    label.pack(pady=20)

    # Mac button
    mac_button = Button(window, text="Mac (700x500)", font=("Arial", 15), command=set_mac_size, bg="white", fg="black", width=20)
    mac_button.pack(pady=10)

    # Windows button
    windows_button = Button(window, text="Windows (800x520)", font=("Arial", 15), command=set_windows_size, bg="white", fg="black", width=20)
    windows_button.pack(pady=10)

    # Linux button
    linux_button = Button(window, text="Linux (900x600)", font=("Arial", 15), command=set_linux_size, bg="white", fg="black", width=20)
    linux_button.pack(pady=10)

    # Back button to return to main screen
    back_button = Button(window, text="Back", font=("Arial", 12), command=show_play_screen, bg="white", fg="black", width=10)
    back_button.pack(pady=20)

# Functions to set window sizes
def set_mac_size():
    window.geometry("700x500")
    messagebox.showinfo("Settings", "Window size set to Mac (700x500)")

def set_windows_size():
    window.geometry("800x520")
    messagebox.showinfo("Settings", "Window size set to Windows (800x520)")

def set_linux_size():
    window.geometry("900x600")
    messagebox.showinfo("Settings", "Window size set to Linux (900x600)")

window.mainloop()
