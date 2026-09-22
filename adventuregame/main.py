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
        if current_scene == "__return__":
            return
        player.current_scene = current_scene

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
    command = input("Valitse (1-4): ")

    if command == "1":
        start_game()
    elif command == "2":
        typed_name = input("Syötä nimi: ")
        if save.save_exists_for(typed_name):
            loaded_player = save.load_game(typed_name)
            run_game(loaded_player)
        else:
            print("Tallennusta ei löytynyt tälle nimelle.")
            input("\nPaina enter palataksesi päävalikkoon.")
    elif command == "3":
        play_guide()
    elif command == "4":
        print("Kiitos kun pelasit")
        sys.exit()
    else:
        print("Väärä syöte")