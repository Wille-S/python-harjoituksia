while True:
    nimi = input("Syötä nimi:")
    if not nimi:
        print("Nimi ei voi olla tyhjä, yritä uudelleen.")
    else:
        break

while True:
    ikä = input("Syötä ikä:")
    if not ikä.isdigit():
        print("Ikä ei ole numero, yritä uudelleen.")
    else:
        ikä = int(ikä)
        break

print(f"Nimi: {nimi}, ikä: {ikä}")