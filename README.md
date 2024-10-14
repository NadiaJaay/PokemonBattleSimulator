Setting up the project in VSCode

Inside your project directory, create a folder named .vscode to store VSCode configuration settings.

Name this folder .vscode (make sure to include the dot at the beginning).
Inside the .vscode folder, create a new file named settings.json:

Right-click on the .vscode folder and choose New File.
Name the file settings.json.

Then, copy and paste the following configuration into the settings.json file:

{
    "python.pythonPath": "C:/Users/Nadia/AppData/Local/Programs/Python/Python313/python.exe",
    "python.envFile": "${workspaceFolder}/.env",
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}/src"
    }
}
