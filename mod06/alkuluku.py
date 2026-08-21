luku = int(input("Syötä kokonaisluku: "))

on_alkuluku = True

if luku < 2:
    on_alkuluku = False
else:
    for i in range (2, luku):
        if luku % i == 0:
            on_alkuluku = False
            break

if on_alkuluku:
    print("On alkuluku")
else:
    print("Ei ole alkuluku")
