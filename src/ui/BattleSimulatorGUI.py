# BattleSimulatorGUI.py
from tkinter import *
import pygame
from models.pokemon import Pokemon  # Import the Pokemon model

# window config
window = Tk()
window.geometry("700x500")
window.title("PokemonBattleSimulator")
window.config(background="#FFDD57")

# Function to handle Pokémon selection
def select_pokemon(pokemon_name):
    # Clear current screen
    for widget in window.winfo_children():
        widget.destroy()
    selected_label = Label(window, text=f"You selected {pokemon_name}!", font=('Arial', 30), fg='green')
    selected_label.pack(pady=100)

# Function to start the battle and show Pokémon selection buttons
def start_battle():
    # Clear current screen
    for widget in window.winfo_children():
        widget.destroy()

    # Fetch Pokémon from the database using the model
    pokemon_options = Pokemon.get_pokemon_list()

    label = Label(window, text="Select a Pokémon...", font=("Ariel", 40), bg="#FFDD57", fg="black")
    label.pack(side=BOTTOM, padx=70, pady=100)

    # Add pokemon image buttons
    for pokemon in pokemon_options:
        if pokemon.name == "Charizard":
            charizard_image = PhotoImage(file="../images/charizard.png").subsample(5, 5)
            charizard_button = Button(window, image=charizard_image, bg="#FFDD57", command=lambda p=pokemon.name: select_pokemon(p))
            charizard_button.image = charizard_image
            charizard_button.pack(side=LEFT, padx=45)
        elif pokemon.name == "Blastoise":
            blastoise_image = PhotoImage(file="../images/blastoise.png").subsample(8, 8)
            blastoise_button = Button(window, image=blastoise_image, bg="#FFDD57", command=lambda p=pokemon.name: select_pokemon(p))
            blastoise_button.image = blastoise_image
            blastoise_button.pack(side=LEFT, padx=45)
        elif pokemon.name == "Venusaur":
            venusaur_image = PhotoImage(file="../images/venusaur.png").subsample(8, 8)
            venusaur_button = Button(window, image=venusaur_image, bg="#FFDD57", command=lambda p=pokemon.name: select_pokemon(p))
            venusaur_button.image = venusaur_image
            venusaur_button.pack(side=LEFT, padx=45)

# Function to show the play screen after agreeing to the disclaimer
def show_play_screen():
    # Clear current screen
    for widget in window.winfo_children():
        widget.destroy()

    logo_image_play = PhotoImage(file="../images/PokemonLogo.png")
    logo_label_play = Label(window, image=logo_image_play, bg="#FFDD57")
    logo_label_play.image = logo_image_play
    logo_label_play.pack()

    logo_image_play = PhotoImage(file="../images/BattleImg.png")
    logo_label_play = Label(window, image=logo_image_play, bg="#FFDD57")
    logo_label_play.image = logo_image_play
    logo_label_play.pack()

    pokemon_image_play = PhotoImage(file="../images/umbreon.png").subsample(5, 5)
    pokemon_label_play = Label(window, image=pokemon_image_play, bg="#FFDD57")
    pokemon_label_play.image = pokemon_image_play
    pokemon_label_play.pack()

    # Create Play Screen with a Play Button
    pygame.mixer.init()
    def play_music():
        pygame.mixer.music.load("../sfx/10 Relic Song.mp3")
        pygame.mixer.music.play(-1)

    def stop_music():
        pygame.mixer.music.stop()

    def toggle_music():
        if pygame.mixer.music.get_busy():
            stop_music()
        else:
            play_music()

    sound_img = PhotoImage(file="../images/sound.png").subsample(20, 20)
    sound_button = Button(window, image=sound_img, command=toggle_music, bg="#FFDD57", borderwidth=0, highlightthickness=0)
    sound_button.image = sound_img
    sound_button.pack(side=LEFT, padx=10)

    play_button = Button(window, text="PLAY", font=('Arial', 20), command=start_battle)
    play_button.pack()

# ---------------------
# Load logo and disclaimer
logo_path = "../images/PokemonLogo.png"
logo_image = PhotoImage(file=logo_path)
logo_label = Label(window, image=logo_image, bg="#FFDD57")
logo_label.pack()

battle_img_path = "../images/BattleImg.png"
battle_img = PhotoImage(file=battle_img_path)
battle_img_label = Label(window, image=battle_img, bg="#FFDD57")
battle_img_label.pack()

# Create Disclaimer Frame (for the border)
disclaimer_frame = Frame(window, bd=2, relief="solid", padx=10, pady=10)
disclaimer_frame.pack(pady=20)

disclaimer_label = Label(disclaimer_frame, text="DISCLAIMER", font=('Arial', 30, 'bold'))
disclaimer_label.pack()

disclaimer_text = Label(disclaimer_frame, text="This Pokémon Battle Simulator is a fan-made project and is not affiliated with or endorsed by Nintendo, Game Freak, or The Pokémon Company. All Pokémon characters and related assets are the property of their respective owners. This simulator is created purely for entertainment purposes and is free to use. No copyright infringement is intended.", wraplength=400)
disclaimer_text.pack()

agree_button = Button(disclaimer_frame, text="AGREE", font=('Arial', 20), command=show_play_screen)
agree_button.pack(pady=20)

window.mainloop()
