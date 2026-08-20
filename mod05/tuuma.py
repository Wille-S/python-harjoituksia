while True:
    syöte = input("Montako tuumaa? ")
    if not syöte.replace("-", "", 1).replace(".", "", 1).isdigit():
        print("Ei numero, yritä uudelleen.")
        continue
    tuuma = 2.54
    tuumat = float(syöte)

    if tuumat < 0:
        break
    elif not isinstance(tuumat, (int, float)):
        print("Ei numero, yritä uudelleen")
    else:
        sentit = tuumat * tuuma
        print(str(sentit) + "cm")