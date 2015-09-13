# DO NOT MODIFY THIS
NONE = 0
SHORT_UP = 1
LONG_UP = 2
SHORT_DOWN = 3
LONG_DOWN = 4
SHORT_LEFT = 5
LONG_LEFT = 6
SHORT_RIGHT = 7
LONG_RIGHT = 8
SHORT_SELECT = 9
LONG_SELECT = 10
NO_BUTTON_TO_SPECIFY = 999

# You can play with these settings but be careful with the first 3
TIME_FOR_LONG_PRESS = 0.5
SLEEP_AFTER_LONG_PRESS = 0.2
SLEEP_AFTER_SHORT_PRESS = 0.2
SLEEP_AFTER_MESSAGE = 2

# Use these settings to set an action to a key. You can also try the alternative settings.
TOP_VIEW_NEXT_ITEM = SHORT_RIGHT
TOP_VIEW_PREVIOUS_ITEM = SHORT_LEFT
TOP_VIEW_SELECT = SHORT_SELECT
TOP_VIEW_RETURN_TOP_VIEW = NO_BUTTON_TO_SPECIFY
SUB_VIEW_NEXT_ITEM = SHORT_DOWN
SUB_VIEW_PREVIOUS_ITEM = SHORT_UP
SUB_VIEW_SELECT = SHORT_SELECT
SUB_VIEW_RETURN = LONG_SELECT
SUB_VIEW_RETURN_TOP_VIEW = NO_BUTTON_TO_SPECIFY
SHOW_GAMES_NEXT_GAME = SHORT_DOWN
SHOW_GAMES_PREVIOUS_GAME = SHORT_UP
SHOW_GAMES_NEXT_LETTER = LONG_DOWN
SHOW_GAMES_PREVIOUS_LETTER = LONG_UP
SHOW_GAMES_UPLOAD_DEFAULT = SHORT_SELECT
SHOW_GAMES_CHOOSE_SYSTEM_TO_UPLOAD = SHORT_RIGHT
SHOW_GAMES_ADD_REMOVE_FAVORITES = LONG_RIGHT
SHOW_GAMES_RETURN = LONG_SELECT
SHOW_GAMES_RETURN_TOP_VIEW = NO_BUTTON_TO_SPECIFY
CHOOSE_SYSTEM_TO_UPLOAD_NEXT_ITEM = SHORT_DOWN
CHOOSE_SYSTEM_TO_UPLOAD_PREVIOUS_ITEM = SHORT_UP
CHOOSE_SYSTEM_TO_UPLOAD_SELECT = SHORT_SELECT
CHOOSE_SYSTEM_TO_UPLOAD_RETURN = LONG_SELECT
CHOOSE_SYSTEM_TO_UPLOAD_RETURN_TOP_VIEW = NO_BUTTON_TO_SPECIFY
PING_SHORTCUT = NO_BUTTON_TO_SPECIFY
PING_NEXT_ITEM = SHORT_DOWN
PING_PREVIOUS_ITEM = SHORT_UP
PING_SELECT = SHORT_SELECT
PING_RETURN = LONG_SELECT
PING_RETURN_TOP_VIEW = NO_BUTTON_TO_SPECIFY
UNKNOWN_ROMS_NEXT_ITEM = SHORT_DOWN
UNKNOWN_ROMS_PREVIOUS_ITEM = SHORT_UP
UNKNOWN_ROMS_SELECT = SHORT_SELECT
UNKNOWN_ROMS_RETURN = LONG_SELECT
UNKNOWN_ROMS_RETURN_TOP_VIEW = NO_BUTTON_TO_SPECIFY
UNKNOWN_ROMS_CHOOSE_GAME_NEXT_GAME = SHORT_DOWN
UNKNOWN_ROMS_CHOOSE_GAME_PREVIOUS_GAME = SHORT_UP
UNKNOWN_ROMS_CHOOSE_GAME_NEXT_LETTER = LONG_DOWN
UNKNOWN_ROMS_CHOOSE_GAME_PREVIOUS_LETTER = LONG_UP
UNKNOWN_ROMS_CHOOSE_GAME_SELECT_GAME = SHORT_SELECT
UNKNOWN_ROMS_CHOOSE_GAME_RETURN = LONG_SELECT
UNKNOWN_ROMS_CHOOSE_GAME_RETURN_TOP_VIEW = NO_BUTTON_TO_SPECIFY

# Alternative configuration with vertical menus
#TOP_VIEW_NEXT_ITEM = SHORT_DOWN
#TOP_VIEW_PREVIOUS_ITEM = SHORT_UP
#TOP_VIEW_SELECT = SHORT_RIGHT
#TOP_VIEW_RETURN_TOP_VIEW = SHORT_LEFT
#SUB_VIEW_NEXT_ITEM = SHORT_DOWN
#SUB_VIEW_PREVIOUS_ITEM = SHORT_UP
#SUB_VIEW_SELECT = SHORT_RIGHT
#SUB_VIEW_RETURN = LONG_SELECT
#SUB_VIEW_RETURN_TOP_VIEW = SHORT_LEFT
#SHOW_GAMES_NEXT_GAME = SHORT_DOWN
#SHOW_GAMES_PREVIOUS_GAME = SHORT_UP
#SHOW_GAMES_NEXT_LETTER = LONG_DOWN
#SHOW_GAMES_PREVIOUS_LETTER = LONG_UP
#SHOW_GAMES_UPLOAD_DEFAULT = SHORT_SELECT
#SHOW_GAMES_CHOOSE_SYSTEM_TO_UPLOAD = 
#SHOW_GAMES_RETURN = SHORT_LEFT
#SHOW_GAMES_RETURN_TOP_VIEW = LONG_SELECT
#CHOOSE_SYSTEM_TO_UPLOAD_NEXT_ITEM = SHORT_DOWN
#CHOOSE_SYSTEM_TO_UPLOAD_PREVIOUS_ITEM = SHORT_UP
#CHOOSE_SYSTEM_TO_UPLOAD_SELECT = SHORT_SELECT
#CHOOSE_SYSTEM_TO_UPLOAD_RETURN = SHORT_LEFT
#CHOOSE_SYSTEM_TO_UPLOAD_RETURN_TOP_VIEW = LONG_SELECT
#PING_SHORTCUT = NO_BUTTON_TO_SPECIFY
#PING_NEXT_ITEM = SHORT_DOWN
#PING_PREVIOUS_ITEM = SHORT_UP
#PING_SELECT = SHORT_SELECT
#PING_RETURN = SHORT_LEFT
#PING_RETURN_TOP_VIEW = LONG_SELECT
#UNKNOWN_ROMS_NEXT_ITEM = SHORT_DOWN
#UNKNOWN_ROMS_PREVIOUS_ITEM = SHORT_UP
#UNKNOWN_ROMS_SELECT = SHORT_SELECT
#UNKNOWN_ROMS_RETURN = SHORT_LEFT
#UNKNOWN_ROMS_RETURN_TOP_VIEW = LONG_SELECT
#UNKNOWN_ROMS_CHOOSE_GAME_NEXT_GAME = SHORT_DOWN
#UNKNOWN_ROMS_CHOOSE_GAME_PREVIOUS_GAME = SHORT_UP
#UNKNOWN_ROMS_CHOOSE_GAME_NEXT_LETTER = LONG_DOWN
#UNKNOWN_ROMS_CHOOSE_GAME_PREVIOUS_LETTER = LONG_UP
#UNKNOWN_ROMS_CHOOSE_GAME_SELECT_GAME = SHORT_SELECT
#UNKNOWN_ROMS_CHOOSE_GAME_RETURN = SHORT_LEFT
#UNKNOWN_ROMS_CHOOSE_GAME_RETURN_TOP_VIEW = LONG_SELECT

# List of your systems with the IPs. You have to change this setting depending on your systems, but keep in mind 
# to also change the "SYSTEMS" item on each game system categories. 
SYSTEMS_FOR_UPLOAD = { 
        "Naomi 1 #1":   "192.168.1.2",
        "Naomi 2 #1":   "192.168.1.3",
        "Naomi 2 #2":   "192.168.1.4",
        "Naomi 2 #3":   "192.168.1.5",
        "Triforce #1":  "192.168.1.6",
        "Chihiro":      "192.168.1.7"
    }

# Set absolute path of rom files ending with trailing /
ROM_DIR = "/boot/roms/"  

# Set absolute path of the file containing the list your favorites games
FAVORITES_FILE = "/boot/piforcetools/favorites"  

# Set it to one of the language defined in "LABELS"
LANGUAGE = "en"

# Wether the welcome message is shown or not
SHOW_WELCOME_MESSAGE = True

# Define if you want the programm to remove the games without bin files
PURGE_GAMES = True

# Define if you want the programm to remove systems that couldn't be found in SYSTEMS_FOR_UPLOAD
PURGE_SYSTEMS = True