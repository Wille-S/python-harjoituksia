import random
pisteet = int(input("Pisteiden määrä: "))

n = 0
i = 0

while i < pisteet:
    x = random.uniform(1, -1)
    y = random.uniform(1, -1)

    if x**2 + y**2 < 1:
        n += 1

    i += 1

pii_arvio = 4 * n / pisteet

print(f"Piin likiarvo {pisteet} pisteellä on: {pii_arvio}")