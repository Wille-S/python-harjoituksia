sukupuoli = input("Syötä biologinen sukupuoli (Mies/Nainen):").lower()
hemoglobiini = int(input("Syötä hemogloobini arvosi (g/l):"))

if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini arvosi ovat alhaiset")
    elif hemoglobiini > 195:
        print("Hemoglobiini arvosi ovat korkeat")
    else:
        print("Hemoglobiini arvosi ovat normaalit")
elif sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini arvosi ovat alhaiset")
    elif hemoglobiini > 175:
        print("Hemoglobiini arvosi ovat korkeat")
    else:
        print("Hemoglobiini arvosi ovat normaalit")