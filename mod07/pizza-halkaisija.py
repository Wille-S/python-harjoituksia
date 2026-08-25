import math

def pizza_euro_neliömetri(halkaisija, hinta):
    x = halkaisija / 2
    y = x ** 2
    z = math.pi * y

    ms = z / 10000
    hinta_neliömetreinä = hinta / ms
    return(hinta_neliömetreinä)

a_halkaisija = float(input("Ensimmäisen pizzan halkaisija sentteinä: "))
a_hinta = float(input("Ensimmäisen pizzan hinta euroina: "))
b_halkaisija = float(input("Toisen pizzan halkaisija sentteinä: "))
b_hinta = float(input("Toisen pizzan hinta euroina: "))

pizza_a = pizza_euro_neliömetri(a_halkaisija, a_hinta)
pizza_b = pizza_euro_neliömetri(b_halkaisija, b_hinta)

if pizza_a < pizza_b:
    print("Ensimmäinen pizza on parempi vastine rahalle.")
elif pizza_a > pizza_b:
    print("Toinen pizza on parempi vastine rahalle.")
else:
    print("Pizzoilla on sama vastine rahalle")
