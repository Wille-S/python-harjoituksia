import save
from player import Weapon

GLOBAL_COMMANDS = ["status", "tallenna", "ohje", "päävalikko"]

def change_weapon(player, new_weapon):
    print(f"Vaihoit aseen {player.weapon} aseeseen {new_weapon}")
    player.weapon = new_weapon
    
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
            print("HP: " + str(player.health))
            print("Tavarat: " + str(player.items))
        if decision in options:
            return decision
        else:
            print("Ei toimiva komento")

def load_scene1a(player):
    username = player.username
    print("Heräsit juuri ja et muista muuta kuin nimesi, " + username)
    decision = choice(
        "Löydät itsesi hirsimökistä. Mitä haluat tehdä? Tutki huonetta (T)) tai lähde ulos (U): ",
        ["t", "u"], player
    )

    if decision == "u":
        return "frontyard"
    elif decision == "t":
        return "room"

def load_scene1b(player):
    decision = choice(
        "Katsot ympärillesi ja löydät pampun(ase)(P) ja karkkia(K), päätät ottaa mukaan jomman kumman ja lähteä ulos: ",
        ["p", "k"], player
    )
    if decision == "p":
        change_weapon(player, Weapon("Pamppu", (4, 8)))
        player.items.append("pamppu")
    elif decision == "k":
        player.items.append("karkki")
    return "frontyard"

def load_scene2(player):
    print(player.items)
    decision = choice(
        "Olet hirsimökin ulkopuolella ja näät edessäsi kyltin, joka osoittaa kahta eri polkua, vasen kylään(V) ja oikea luolaan(O), mihin menet?: ",
        ["v", "o"], player
    )
    if decision == "V":
        return "village"
    if decision == "O":
        return "cave"

def load_scene3_1(player):
    print("lorem ipsum")

def load_scene3_2(player):
    print("lorem ipsum")

scene_map = { # map of all scenes
    "start" : load_scene1a,
    "room" : load_scene1b,
    "frontyard" : load_scene2,
    "village" : load_scene3_1,
    "cave" : load_scene3_2,
}