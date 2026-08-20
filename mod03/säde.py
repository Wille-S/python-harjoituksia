import math
while True:
    try:
        r = float(input("Syötä ympyrän säde:"))
        break
    except ValueError:
        print("Tämä ei ole numero, yritä uudelleen.")

p = math.pi * r**2

print ("Ympyrän pinta-ala on " + str(p) + ".")