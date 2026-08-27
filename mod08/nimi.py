nimet = set()
nimi = input("Syötä nimi, jätä tyhjäksi lopettaaksesi: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print("Uusi nimi")
    nimi = input("Syötä nimi, jätä tyhjäksi lopettaaksesi: ")
for nimi in nimet:
    print(nimi)