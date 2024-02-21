# Le Homebrew France - Lumia
A multipurpose Discord Bot for "Le Homebrew France" server.

# Features
- Nintendo Switch Serial number checker (IMSP)
- PS3 Model Number checker (tells if a PS3 can run CFW or not)
- Moderation commands (mute, tempban, ban)
- Generic commands
- Homebrew commands (guides, packs, etc.)

# Setting up the bot

- Go to [Discord Developer Portal](https://discord.com/developers/applications).
- Create a new application with the name of the bot you want to create.
- Create your bot.
- Give the bot "Administrator" permissions.
- Copy the token.
- Replace ``{BOT_TOKEN}`` in the code with your bot's token. 
- Replace all the roles IDs with the corresponding ones on your server. 

# Running the bot
### On Windows 

- Download the [latest version of Python](https://www.python.org/downloads/)
- Unzip the source code's archive.
- Open "Lumia Bot Launcher.exe".
- Click on "Modules", it will install the necessary modules to run the bot.
- Click on "Exécuter".

### On Linux 

- Open a terminal
- Install python3 with the following command line : ``sudo apt-get install python3``
- Install python3-pip with the following command line : ``sudo apt-get install python3-pip``
- Install the "Discord" Python module with the following command line : ``pip3 install discord``
- Run the bot from the "Lumia-Discord-Bot" folder.
- Execute the bot with ``python3 main.py``
