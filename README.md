# Pokémon Battle Simulator

The Pokémon Battle Simulator is a simple GUI-based application built using Python and Tkinter. It allows players to simulate battles between their Pokémon and the computer's Pokémon, featuring moves, live HP updates, and automatic database management.

## Features
- **Select Pokémon**: Choose a Pokémon from the database to battle.
- **Simulate Battles**: Real-time battle mechanics where:
  - The computer randomly selects one of the last six Pokémon in the database.
  - The system decides who starts first.
  - Moves are selected randomly for the computer.
  - Players manually select moves, with PP tracking.
- **HP and PP Management**: Live updates of Pokémon HP and move PP.
- **Battle Results**: Declares the winner when one Pokémon’s HP reaches 0.
- **Cross-Platform Settings**: GUI supports different screen sizes for macOS, Linux and Windows.
- **Database Auto-Creation**: The application automatically creates the SQLite database and tables if they do not exist.

## Prerequisites
Before setting up the project, ensure you have the following installed:
- Python 3.10 or later
- SQLite (included with Python)
- Tkinter (included with Python)
- Pygame (included with Python)
- IntelliJ IDEA with Python plugin (for running in IntelliJ)


## Setting Up the Project in IntelliJ IDEA

### Step 1: Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/NadiaJaay/PokemonBattleSimulator.git
cd PokemonBattleSimulator
```

### Step 2: Open the Project in IntelliJ IDEA

Open IntelliJ IDEA and click on File > Open.

Navigate to the cloned repository folder and open it.

### Step 3: Configure Python SDK

Go to File > Project Structure > Modules.

Add a Python SDK by selecting + Add SDK and browsing to your Python 3.x installation.

### Step 4: Run the Application

Locate the main Python file (BattleSimulatorGUI.py).

Right-click on the file and select Run 'BattleSimulatorGUI'.

### Step 5: Database Creation

The application will automatically create the SQLite database (pokemonDetails.db) and required tables on the first run. No manual setup is needed.

## Setting Up the Project in VSCode (Optional)

Inside your project directory, create a folder named .vscode.

Inside the .vscode folder, create a file named settings.json.

Add the following configuration to the settings.json file:

```bash

{
    "python.pythonPath": "insert your python path",
    "python.envFile": "${workspaceFolder}/.env",
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}/src"
    }
}
```

## How to Play

#### Step 1: Run the application using the steps above.

#### Step 2: Select your Pokémon from the GUI dropdown.

#### Step 3: Begin the battle:

- Moves will reduce the opponent's HP.

- PP will be updated after each move.

- The system announces the winner when a Pokémon’s HP reaches 0.

## Credits

#### Sounds
- All sounds used in this project are non-copyrighted and sourced from [My Audio Journey](https://www.youtube.com/watch?v=lfr7V1ZDHIU&list=PLKteXd0CosoOXlI-5aHF_KsaHp0aJ5vmn&index=13&ab_channel=MyAudioJourneys).

#### Images
- The images used in this project were obtained from [IMGBIN](https://imgbin.com). 
