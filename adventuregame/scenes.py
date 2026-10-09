import save
from player import Weapon
from enemies import Enemy, Boss
import functions

# GLOBAL_COMMANDS = ["status", "tallenna", "ohje", "päävalikko"]

def change_weapon(player, new_weapon): # changing weapons happens with this function
    print(f"Vaihoit aseen \"{player.weapon.name}\" aseeseen \"{new_weapon.name}\"")
    player.weapon = new_weapon
def pause (text=""):
    if text:
        print(text)
    input("\n[Paina enter jatkaaksesi]") #pause instead of print so you can advance by pressing enter

def load_scene1a(player): # scenes are functions that are mapped in a dictionary at the end of file
    username = player.username
    pause("Heräsit juuri ja et muista muuta kuin nimesi, " + username)
    decision = functions.choice(
        "Löydät itsesi mökistä. Mitä haluat tehdä? Tutki huonetta (t) tai lähde ulos (u): ",
        ["t", "u", "cheat"], player
    )

    if decision == "u":
        return "frontyard"
    elif decision == "t":
        return "room"
    elif decision == "cheat":
        change_weapon(player, Weapon("cheats", (100, 200)))
        return "room"

def load_scene1b(player):
    decision = functions.choice(
        "Katsot ympärillesi ja löydät veitsen(ase)(v) ja pippuri sumutetta(p). Päätät ottaa varmuuden vuoksi mukaan jomman kumman ja lähteä ulos: ",
        ["v", "p"], player
    )
    if decision == "v":
        change_weapon(player, Weapon("veitsi", (4, 8)))
        player.items.append("veitsi")
    elif decision == "p":
        player.items.append("pippuri_sumute")
    return "frontyard"

def load_scene2(player):
    pause("Olet mökin ulkopuolella ja kuulet susien ulvontaa ja taivaalla näät täysikuun.")
    pause("Kävelet jonkun ajan polkua pitkin kunnes törmäät risteykseen. Vieressä olevan kyltin mukaan vasen polkui johtaa kylään ja oikea luolaan.")
    decision = functions.choice(
        "Minne haluat mennä? v/o: ",
        ["v", "o"], player
    )
    if decision == "v":
        return "village"
    if decision == "o":
        return "cave"

def load_scene3_1(player):
    sudet = Enemy("Sudet", 10, (2, 5))
    pause("Olet nyt kylässä, mutta et näe ihmisiä ollenkaan. Kaikki ovet ja ikkunat ovat kiinni.")
    pause("Yhtäkkiä kaksi sutta hyppäsi tiellesi! Joudut taistelemaan.")
    outcome = functions.start_combat(player, sudet)
    if outcome == "lost":
        return functions.handle_game_over(player)
    elif outcome == "won":
        player.animals_defeated +=2
    return "village2"

def load_scene3_1b(player):
    pause("Kävelet kylää eteenpäin kunnes joku ikkunan ja näyttää siltä, että haluaa kertoa jotakin.")
    if player.animals_defeated > 0:
        pause("Menet hänen luokseen ja hän varoittaa sinua taistelemasta susia tai sille saattaa olla seurauksia.")
    elif player.animals_defeated == 0:
        pause("Hän sanoo sinulle, että teit oikein kun vältit susien taistelemista ja kehottaa jatkamaan samaa mallia.")
    pause("Jatkat matkaa ja päädyt kylän loppuun. Tielläsi edessä näet 3 sutta. Voit joko jatkaa tiellä ja törmätä susiin tai kiertää ne kulkemalla metsässä.")
    decision = functions.choice(
        "Mihin päätät mennä? Metsään(m) vai tietä(t)?",
        ["m", "t"], player
    )
    if decision == "m":
        return "forest"
    elif decision == "t":
        return "road"

def load_scene3_2(player):
    susi = Enemy("Susi", 5, (1, 3))
    pause("Kävelet polkua pitkin kunnes törmäät luolaan. Päätät mennä sinne sisään.")
    pause("Luolassa törmäät suteen!")
    outcome = functions.start_combat(player, susi)
    if outcome == "lost":
        return functions.handle_game_over(player)
    elif outcome == "won":
        player.animals_defeated +=1
    pause("Jatkat luolassa syvemmälle ja löydät uloskäynnin sekä miekan jonka avulla susien lyöminen olisi helppoa.")
    decision = functions.choice(
        "Uloskäynnin ulkopuolella kuulet susia. Otatko miekan mukaan lähtiessäsi ulos? k/e",
        ["k", "e"], player
    )
    if decision == "k":
        change_weapon(player, Weapon("miekka", (8, 12)))
        player.items.append("miekka")
        return "road"
    elif decision == "e":
        return "road"

def load_scene4(player):
    sudet = Enemy("Sudet", 15, (3, 7))
    if "miekka" in player.items:
        pause("Sudet näyttävät pelkäävän miekkaa selässsi. Voisit mahdollisesti pelotella sudet pois sillä. Toisaalta taistelun ei pitäisi olla mikään ongelma mahtavan miekkasi kanssa.")
        decision = functions.choice(
            "Yritätkö pelotella sudet pois miekan avulla? k/e",
            ["k", "e"], player
        )
        if decision == "k":
            pause("Heiluttelet miekkaa villisti ympäriinsä ja sudet lähtevät karkuun.")
            pause("Jatkat tietä eteenpäin.")
            return functions.load_ending
        if decision == "e":
            pause("Joudut taistelemaan susia.")
            outcome = functions.start_combat(player, sudet)
            if outcome == "lost":
                return functions.handle_game_over(player)
            elif outcome == "won":
                player.animals_defeated +=3
            pause("Jatkat tietä eteenpäin.")
            return functions.load_ending
    else:
        pause("Joudut taistelemaan susia.")
        outcome = functions.start_combat(player, sudet)
        if outcome == "lost":
            return functions.handle_game_over(player)
        elif outcome == "won":
            player.animals_defeated +=3
        pause("Jatkat tietä eteenpäin.")
        return functions.load_ending

def load_scene5(player):
    pause("Olet metsässä ja etenet hitaasti oksia huitoen eteenpäin.")
    pause("Huomaat maassa ansaan astuneen sudenpennun. Voit joko auttaa sitä tai jättää sen ansan armoille.")
    decision = functions.choice(
        "Autatko pentua? k/e",
        ["k", "e"], player
    )
    if decision == "k":
        player.helped_cub = True
    pause("Jatkat matkaa eteenpäin.")
    return functions.load_ending

def ending_1(player):
    pause("Löydät itse seisomassa suuren ihmissuden edessä.")
    pause("Olento katsoo sinua niinkuin oli päättämässä kohtalostasi.")
    pause("Mieleesi tulee kaikki kohtaamiset susien kanssa joista pakenit ja joita vältit.")
    pause("Jotenkin saat olennolta ymmärretyksi sen, että teit oikeita valintoja ja se huitoo ilmaa, niin kuin kertovakseen sinulle, että voit poistua.")
    pause("Loppu.")

def ending_2(player):
    boss = Boss("Ihmissusi", 40, (3, 6), 0.25)
    pause("Löydät itse seisomassa suuren ihmissuden edessä.")
    pause("Olento katsoo sinua niinkuin oli päättämässä kohtalostasi.")
    pause("Mieleesi tulee kaikki kohtaamiset susien kanssa.")
    if player.helped_cub == True:
        pause("Muistat myös sen, että autoit sudenpentua metsässä.")
    else:
        pause("Ihmissusi hyökkää kimppuusi kostaakseen sutensa")
        outcome = functions.start_combat(player, boss, can_flee=False)
        if outcome == "lost":
            pause("Hävisit voimmakkaalle ihmissudelle ja se söi sinut")
        elif outcome == "won":
            pause("Päihitit ihmissuden.")
    pause("Loppu.")

def ending_3(player):
    boss = Boss("Ihmissusi", 40, (3, 6), 0.25)
    pause("Löydät itse seisomassa suuren ihmissuden edessä.")
    pause("Olento katsoo sinua niinkuin oli päättämässä kohtalostasi.")
    pause("Mieleesi tulee kaikki kohtaamiset susien kanssa ja kuinka monta sutta satutit.")
    pause("Ihmissusi hyökkää kimppuusi kostaakseen sutensa")
    outcome = functions.start_combat(player, boss, can_flee=False)
    if outcome == "lost":
        pause("Hävisit voimmakkaalle ihmissudelle ja se söi sinut")
    elif outcome == "won":
        pause("Päihitit ihmissuden.")
    pause("Loppu.")

scene_map = { # map of all scenes
    "start" : load_scene1a,
    "room" : load_scene1b,
    "frontyard" : load_scene2,
    "village" : load_scene3_1,
    "cave" : load_scene3_2,
    "village2": load_scene3_1b,
    "road": load_scene4,
    "forest": load_scene5,
    "good_ending": ending_1,
    "mid_ending": ending_2,
    "bad_ending": ending_3
}