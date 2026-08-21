import random
arpakuutio_maara = int(input("Arpakuutioiden määrä: "))
arpakuutiot = []

for i in range (arpakuutio_maara):
    arpakuutiot.append(random.randint(1, 6))

summa = sum(arpakuutiot)

print(str(arpakuutio_maara) + " määrällä noppia, heitettiin yhteensä numerot " + str(arpakuutiot) + " joidenka summa on " + str(summa))