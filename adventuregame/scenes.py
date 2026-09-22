def choice(desc, options):
    while True:
        decision = input(desc).lower()
        if decision in options:
            return decision
        else:
            print("Ei toimiva komento")

def load_scene1a(player):
    username = player.username
    print("Heräsit juuri ja et muista muuta kuin nimesi, " + username)
    decision = choice(
        "Löydät itsesi hirsimökistä. Mitä haluat tehdä? Tutki huonetta (T)) tai lähde ulos (U): ",
        ["t", "u"]
    )

    if decision == "u":
        return "frontyard"
    elif decision == "t":
        return "room"

def load_scene1b(player):
    decision = choice(
        "Katsot ympärillesi ja löydät pampun(ase)(P) ja karkkia(K), päätät ottaa mukaan jomman kumman ja lähteä ulos: ",
        ["p", "k"]
    )
    if decision == "p":
        player.items.append("pamppu")
    elif decision == "k":
        player.items.append("karkki")
    return "frontyard"

def load_scene2(player):
    print(player.items)
    decision = choice(
        "Olet hirsimökin ulkopuolella ja näät edessäsi kyltin, joka osoittaa kahta eri polkua, vasen kylään(V) ja oikea luolaan(O), mihin menet?: ",
        ["v", "o"]
    )
    if decision == "V":
        return "village"
    if decision == "O":
        return "cave"

def load_scene3_1(player):
    print("lorem ipsum")

def load_scene3_2(player):
    print("lorem ipsum")

scene_map = {
    "start" : load_scene1a,
    "room" : load_scene1b,
    "frontyard" : load_scene2,
    "village" : load_scene3_1,
    "cave" : load_scene3_2,
}