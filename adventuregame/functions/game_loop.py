import random
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
            
def try_escape(player):
    chance = 0.5  # 50% chance to escape
    if "escape_item" in player.items:  # Check if player has an escape item
        chance = 0.8  # Increase chance to 80% if they have a specific item
    return random.random() < chance  # Return True if escape is successful, False otherwise
            
def start_combat(player, enemy):
    print(f"Törmäsit viholliseen: {enemy.name}!")
    while enemy.is_alive() and player.health > 0:
        print(f"\n{enemy.name} HP: {enemy.health}")
        print(f"Sinun HP: {player.health}")
        decision = choice("Valitse toiminto (h, p): ", ["h", "p"], player)
        
        if decision == "h":
            damage = player.weapon.attack()
            enemy.health -= damage
            print(f"Hyökkäsit {enemy.name} ja teit {damage} vahinkoa!")
            if enemy.is_alive():
                enemy_damage = enemy.attack()
                player.health -= enemy_damage
                print(f"{enemy.name} hyökkäsi ja teki {enemy_damage} vahinkoa sinuun!")
        elif decision == "p":
            print("Yrität paeta...")
            if try_escape(player):
                return True
            else:
                print("Epäonnistuit pakenemisessa!")
                enemy_damage = enemy.attack()
                player.health -= enemy_damage
                print(f"{enemy.name} hyökkäsi ja teki {enemy_damage} vahinkoa sinuun!")
        
    if player.health <= 0:
        print("Hävisit taistelun!")
        return False
    else:
        print(f"Voitit taistelun! {enemy.name} kaatui.")
        return True
    
def handle_game_over(player):
    print("Kaaduit taistelussa. Peli päättyi.")
    while True:
        decision = choice("Yritä taistelua uudelleen? (k/e): ", ["k", "e"], player)
        if decision == "k":
            player.health = 20
            return player.current_scene
        elif decision == "e":
            return "__return__"
        else:
            print("Anna kelvollinen vastaus (kyllä/ei).")