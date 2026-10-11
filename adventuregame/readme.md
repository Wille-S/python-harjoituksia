# Seikkailupeli

Komentorivipohjainen tekstiseikkailuepeli toteutettu Pythonilla

## Pelin idea

Pelaaja herää mökistä täysikuun alla eikä muita muuta kuin nimensä. Matka kulkee mökiltä risteykseen, josta voi mennä luolaan tai kylään ja näistä joko metsään tai tiellä ja lopulta ihmissuden luo. Matkalla tänne kohdataan susia, ja pelaajan valinnat joko taistella, paeta, väistää tai pelastaa näitä vaikuttaa pelin loppuun.

## Tominnallisuudet ja toimintaperiaatteet

### Päävalikko

1. Aloita uusi peli (peli kysyy iän ja nimen, alle 12 vuotiaat eivät pääsen pelaamaan ja tässä tapauksessa ohjelma sulkeutuu)
2. Jatka peliä (syötetään nimi, jolla peli on tallennettu)
3. Ohjeet (luetaan tiedostosta `data/guide.txt`)
4. Lopeta (Sulkee ohjelman)

Päävalikon esittelyteksti luetaan tiedostosta `data/intro.txt`.

### Reitit

Peli alkaa aina samasta paikasta: mökki jossa voi tutkia huonetta ja löytää veitsen tai pippurisumutteen. Ja ulkona risteys jossa valitaan kylä tai luola. Reitit haarautuvat tästä

- **Kylä:** kahden suden taistelu josta voi paeta tai taistella näitä. Kylän jälkeen valitaan joko tie tai metsä
- **Luola:** yhden suden taistelu, jonka jälkeen pelaaja löytää miekan jonka voi ottaa mukaan. Luolasta jatketaan tielle
- **Tie:** kolme sutta joiden taistelun voi välttää jos on löytänyt miekan
- **Metsä:** ansaan jäänyt sudenpentu, jonka voi pelastaa

Pelin loppu määräytyy sen mukaan kuinka monta sutta pelaaja on päihittänyt (`animals_defeated`). Paeta tai väistää voi joka ei kasvata tätä laskuria

| Päihtettyjä susia | Loppu |
|---|---|
| 0 | Hyvä loppu: ihmissusi antaa pelaajan mennä |
| 1 tai 2 | Mahdollisesti hyvä loppu: jos pelaaja on auttanut sudenpentua, ihmissusi päästää pelaan menemään muuten taistelu |
| 3 tai enemmän | Huono loppu: taistelu ihmissutta vastaan |

Taistelusta ihmissuden kanssa ei voi paeta

### Taistelu

Taistelu on vuoropohjainen. Pelaaja voi joko `h` (hyökätä) tai `p` (yrittää paeta). Vahinko arvotaan vahinkovälin sisältä `random.randint`-funktiolla. Pakenemisen todennäköisyys on 50 %, mutta pippurisumuke nostaa sen 90 %:iin. Jos pakeneminen epäonnistuu pääsee vihollinen tekemään vahinkoa pelaajaan. Sen jälkeen kun taistelu on voitettu pelaajan HP palautuu täyteen (20). Jos pelaaja häviää taistelun, hän voi joko yrittää uudelleen tai palata päävalikkoon.

### Komennot

Seuraavat komennot toimivat kaikissa pelin valintakohtauksissa, koska kaikki valinnat toimivat saman `choice()`-funktion kautta:

- `tallenna`: tallentaa pelin json -tiedostoon pelaajan nimen perusteella
- `status`: näyttää pelaajan HP:n ja tavarat
- `ohje`: näyttää lyhyen muistutuksen komennoista
- `päävalikko` palaa päävalikkoon

## Kestävä kehitys

Pelin keskeinen valinta liittyy luonnon ja eläinten kunnioittamiseen: paras loppu saadaan kun pelaaja ei satuta villieläimiä tai auttaa niitä. Pelissä kylän asukas muistuttaa tästä pelaajaa ja pelin lopussa ihmissusi tuomitsee pelaajan valintojensa perusteella. Metsässä pelaaja voi myös auttaa sudenpentua joka voi auttaa positiivisesti lopputulokseen.

## Projektin rakenne

```
adventuregame/
├── main.py             Ohjelma käynnistyy tästä ja se sisältää myös main menu silmukan
├── player.py           Player- ja Weapon-luokat
├── enemies.py          Enemy- ja Boss-luokat
├── scenes.py           Kaikki pelin kohtaukset ja scene_map-sanakirja. Myös pari auttavaa funktiota
├── save.py             Pelin tallennus ja lataus (JSON) logiikka, myös oma GameEncoder omia luokkia varten
├── constants.py        Vakituiset tiedostopolut
├── functions/          Paketti jossa pelin funktioita
│   ├── __init__.py     Vie funktiot ulos jotta niitä voi kutsua esim. functions.choice()
│   ├── menu.py         Päävalikkoon liittyvät funktiot
│   └── game_loop.py    Pelin pääsilmukka, uuden pelin aloitus, choice(), taistelulogiikka, ending-logiikka ja peli ohi logiikka
└── data/
    ├── intro.txt       Intro teksti joka tulostuu päävalikossa
    ├── guide.txt       Ohjeteksti
    └── (save.json)     Jos pelaaja on tallentanut niin täällä tallenustiedot
```

### Miksi rakenne näin?

Tiedostot on jaettu pääosin vastuualueiden mukaisesti. Luokat (`player.py`, `enemies.py`), tarina (`scenes.py`), tallennus(`save.py`) ja pelin logiikka (`functions/`) ovat omissa paikoissaan niin asioita on helppoo muuttaa ja korjata. `functions` on Python-paketti. `data/` kansioon on koottu tiedostot, joita ohjelma lukee tai kirjoittaa ja `constants.py` pitää näiden tiedostojen polut yhdessä paikassa. 

## Luokat ja oliot

- **`Player`:** käyttäjänimi esineet, HP, nykyinen kohtaus, ase, päihitettyjen susien määrä, sekä flag siitä onko sudenpentua autettu
- **`Weapon`:** nimi, vahinkoväli ja metodi `attack()`. `Player`:llä on yksi ase (has-a) ja asetta vaihetaan sijoittamalla uusi olio `player.weapon`-attribuuttiin
- **`Enemy`:** nimi, HP ja vahinkoväli sekä metodit `attack()` ja  `is_alive()`.
- **`Boss(Enemy)`:** periytyy `Enemy`-luokasta (is-a) ja ylikirjoittaa `attack()`-metodin niin että vahinko voi tuplaantua tietyllä todennäköisyydellä

## Tallennuslogiikka

Peli tallennetaan JSON-muodossa tiedostoon `data/save.json` käyttäjänimen mukaan, joten yhteen tiedostoon mahtuu useamman pelaajan tallennukset.

`json`-moduuli ei osaa muuttaa `Weapon`-oliota JSONiksi, joten `save.py`:ssä on oma `GameEncoder`-luokka (periytyy `json.JSONENCODER`-luokasta), jonka metodi `default()` muuttaa aseen sanakirjaksi. Latauksessa JSON palauttaa tavallallisia sanakirjoja joten `load_game()` rakentaa `Player`- ja `Weapon`-oliot uudestaan. 

## Käyttö

Ohjelma käynnistetään juurikansiosta `/adventuregame`

```
python main.py
```

...
