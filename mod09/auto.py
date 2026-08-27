import random

class Auto:
    def __init__(self, rekkari, huippu_nopeus, tämänhetkinen_nopeus = 0, matka = 0):
        self.rekkari = rekkari
        self.huippu_nopeus = huippu_nopeus
        self.tämänhetkinen_nopeus = min(max(0, tämänhetkinen_nopeus),huippu_nopeus)
        self.matka = matka
    
    def kiihdytä(self, kmh):
        self.tämänhetkinen_nopeus = min(max(0, self.tämänhetkinen_nopeus + kmh), self.huippu_nopeus)

    def kulje(self, tunnit):
        self.matka = self.matka + tunnit * self.tämänhetkinen_nopeus

uusi_auto = Auto("ABC-123", 142)

# 4.
kilpa_autot = []
n = 0
for i in range(10):
    n += 1
    h = random.randint(100, 200)
    kilpa_auto = Auto("ABC-" + str(n), h)
    kilpa_autot.append(kilpa_auto)
while not any(kilpa_auto.matka >= 10000 for kilpa_auto in kilpa_autot):
    for kilpa_auto in kilpa_autot:
        k = random.randint(-10, 15)
        kilpa_auto.kiihdytä(k)
        kilpa_auto.kulje(1)
for kilpa_auto in kilpa_autot:
    print(f"Rekkari: {kilpa_auto.rekkari} ---------- kuljettu matka: {kilpa_auto.matka}")

# 2.
uusi_auto.kiihdytä(30)
uusi_auto.kiihdytä(70)
uusi_auto.kiihdytä(50)
print(f"Nopeus: {uusi_auto.tämänhetkinen_nopeus}")
uusi_auto.kiihdytä(-200)
print(f"Nopeus: {uusi_auto.tämänhetkinen_nopeus}")

# 3.
uusi_auto.kiihdytä(60)
uusi_auto.kulje(1.5)
print(f"Kuljettu matka: {uusi_auto.matka}")

print(f"Auton rekisteri: {uusi_auto.rekkari}, huippu nopeus: {uusi_auto.huippu_nopeus}km/h, tämänhetkinen nopeus: {uusi_auto.tämänhetkinen_nopeus}km/h ja ajettu matka: {uusi_auto.matka}km.")