import sys
import os
import player
import save
import scenes

def clear_screen(): # function to clear console before eg. main_menu and play_guide
    os.system("cls" if os.name == "nt" else "clear") #both windows and unix covered just in case

def main_menu():
    clear_screen()
    print("-----Päävalikko-----")
    print("Valitse syöttämällä valintaa vastaava numero.")
    print("1. Aloita uusi peli")
    print("2. Jatka peliä")
    print("3. Ohjeet")
    print("4. Lopeta")

def play_guide(): #wip
    clear_screen()
    print("Lorem Ipsum")
    input("\n\nPaina enter paltaksesi päävalikkoon.")

def run_game(player):
    scene_dictionary = scenes.scene_map
    current_scene = player.current_scene
    while current_scene is not None:
        current_scene = scene_dictionary[current_scene](player)

def start_game():
    clear_screen()
    while True:
        try:
            age = int(input("Syötä ikä: "))
        except(ValueError): # print error and try again if age not number
            print("Iän täytyy olla numero.")
            continue
        if age < 12:
            print("Olet liian nuori pelataksesi peliä. K12")
            sys.exit() #if age not over 12 or over just close program(maybe better to just throw back into main menu?)
        while True:
            username = input("Syötä nimi: ")
            if len(username) < 3: #username has to be 3 letters or more
                print("Nimen täytyy olla ainakin kolme merkkiä pitkä.")
            else:
                break
        break
    new_player = player.Player(username) #initialize new player
    run_game(new_player)

while True:
    main_menu()
    choice = input("Valitse (1-4): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        if save.save_exist():
            pass ## todo
        else:
            print("Tallennusdataa ei ole")
            input("\nPaina enter palataksesi päävalikkoon.")
    elif choice == "3":
        play_guide()
    elif choice == "4":
        print("Kiitos kun pelasit")
        sys.exit()
    else:
        print("Väärä syöte")