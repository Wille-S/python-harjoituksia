hytti_luokka = input("Syötä hyttiluokka (LUX, A, B, C):").upper()

if hytti_luokka == "LUX":
    print("LUX on parvekkeellinen hytti autokannen yläkannella.")
elif hytti_luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti_luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti_luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
