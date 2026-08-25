def galloona_litroiksi(n):
    global litra
    litra = n * 3.785

while True:
    syöte = input("Montako galloonaa? ")
    if not syöte.replace("-", "", 1).replace(".", "", 1).isdigit():
        print("Ei numero, yritä uudelleen.")
        continue
    galloonat = float(syöte)

    if galloonat < 0:
        break
    else:
        galloona_litroiksi(galloonat)
        print(str(litra) + " litraa")