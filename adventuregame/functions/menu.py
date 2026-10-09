import os
from constants import INTRO_PATH, GUIDE_PATH

def clear_screen(): # function to clear console before eg. main_menu and play_guide
    os.system("cls" if os.name == "nt" else "clear") #both windows and unix covered just in case

def main_menu(): # main menu function prints intro.txt in /data
    clear_screen()
    with open(INTRO_PATH, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

def play_guide(): #play guide functions prints guide.txt in /data
    clear_screen()
    with open(GUIDE_PATH, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
    input("\n\nPaina enter paltaksesi päävalikkoon.")