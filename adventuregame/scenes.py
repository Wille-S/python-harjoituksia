def choice(desc, options):
    while True:
        decision = input(desc).lower
        if decision in options:
            return decision
        else:
            print("Ei toimiva komento")

def load_scene1(player):
    username = player.username
    print("Heräsit juuri ja et muista muuta kuin nimesi, " + username)
    decision_1 = choice(
        "Löydät itsesi hirsimökistä. Mitä haluat tehdä? Tutki huonetta (T)) tai lähde ulos (U): ",
        ["t", "u"]
    )

    if decision_1 == "t":
        print("lorem ipsum")
    elif decision_1 == "u":
        print("lorem ipsum")

scene_map = {
    "start" : load_scene1,
}