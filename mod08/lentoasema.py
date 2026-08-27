lentoasemat = {
    "EFHK": "Helsinki-Vantaa"}

def lisää_asema(icao, nimi):
    if icao in lentoasemat:
        print("ICAO on jo lentoasema listassa")
    elif nimi in lentoasemat.values():
        print("Nimi on jo lentoasema listassa")
    else:
        lentoasemat[icao] = nimi

def hae_asema(icao):
    if icao in lentoasemat:
        print(lentoasemat[icao])
    else:
        print("Ei ole olemassa")

while True:
    print("Valitse toiminto (1-2)")
    print("1. Lisää lentoasema")
    print("2. Hae lentoasemaa ICAO perusteella")
    print("3. Lopeta")

    syöte = input("1, 2 tai 3: ")

    if syöte == "1":
        i = input("Icao: ")
        a = input("Lentoaseman nimi: ")
        lisää_asema(i, a)
    elif syöte == "2":
        h = input("Icao: ")
        hae_asema(h)
    elif syöte == "3":
        break
