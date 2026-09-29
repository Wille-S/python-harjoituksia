import functions
import scenes
import player
import sys
import save

def run_game(player): #core game loop
    scene_dictionary = scenes.scene_map
    current_scene = player.current_scene
    while current_scene is not None:
        current_scene = scene_dictionary[current_scene](player)
        if current_scene == "__return__":
            return
        player.current_scene = current_scene

def start_game():
    functions.clear_screen()
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

def choice(desc, options, player):
    while True:
        decision = input(desc).lower()

        if decision == "tallenna":
            save.save_game(player)
            print("Tallennettu.")
            continue
        elif decision == "ohje":
            print("tallenna = tallenna peli, päävalikko = palaa päävalikkoon......")
            continue
        elif decision == "päävalikko":
            return "__return__"
        elif decision == "status":
            print(f"HP: {player.health}")
            print("Tavarat: " + str(player.items))
            continue
        if decision in options:
            return decision
        else:
            print("Ei toimiva komento")