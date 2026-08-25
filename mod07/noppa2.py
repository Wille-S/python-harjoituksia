import random
tahkom = int(input("Tahkojen yhteismäärä: "))
def noppa_heitto(n):
    global noppa 
    noppa = random.randint(1, n)

while True:
    noppa_heitto(tahkom)
    if noppa == tahkom:
        print(str(noppa))
        break
    else:
        print(str(noppa))