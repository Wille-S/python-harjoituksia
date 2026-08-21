import sys
# Kysytään nimi ja ikä
while True:
    name = input("Syötä nimi: ")
    age = int(input("Syötä ikä: "))
    while len(name) < 3:
        print("Nimen täytyy olla ainakin 3 merkkiä pitkä")
        name = input("Syötä nimi: ")
    if age < 12:
        print("Olet liian nuori pelataksesi peliä. Peli on k-12.")
        sys.exit()
    print("Tervetuloa!")
    break
# Päävalikko
while True:
    print("--Päävalikko--")
    print("Syötä komento")
    print("1. Aloita")
    print("2. Ohjeet")
    print("3. Lopeta")

    komento = input("Valitse(1-3): ")

    if komento == "1":
        print("Peli alkaa")
    elif komento == "2":
        print("lorem ipsum")
    elif komento == "3":
        print("Kiitos kun pelasit")
        sys.exit()
    else:
        print("Ei komento, yritä uudelleen.")