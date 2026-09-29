# Seikkailupeli

## Mitä pelissä tehdään

**TODO**

## Kestävä kehitys

**TODO**

## Projektin rakenne

```
adventuregame/
├── main.py             Ohjelma käynnistyy tästä ja se sisältää myös main menu silmukan
├── player.py           Player sekä Weapon luokka
├── enemies.py          Vihollisluokat ml. mahdollinen pomo **TODO**
├── scenes.py           Pelin eri kohtaukset ja niiden logiikka
├── save.py             Pelin tallennus sekä jatkamis logiikka, myös oma json encoder omia luokkia varten
├── constants.py        Vakituiset tiedostopolut
├── functions/          Paketti jossa pelin funktioita
│   ├── __init__.py     Vie funktiot ulos jotta niitä voi kutsua esim. functions.choice
│   ├── menu.py         Päävalikkoon liittyvät funktiot
│   └── game_loop.py    Pelin pääsilmukka ja uuden pelin aloitus
└── data/
    ├── intro.txt       Intro teksti joka tulostuu päävalikossa
    ├── guide.txt       Ohje teksti **TODO*
    └── (save.json)     Jos pelaaja on tallentanut niin täällä tallenustiedot
```

### Miksi näin?

**TODO**

## Luokat ja oliot

...

## Tallennuslogiikka

...
