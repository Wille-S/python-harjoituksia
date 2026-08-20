while True:
    try:
        kanta = float(input("Syötä suorakulmion kanta senttimetreissä:"))
        korkeus = float(input("Syötä suorakulmion korkeus senttimetreissä:"))
        break
    except ValueError:
        print("Tämä ei ole numero, yritä uudelleen.")

pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

print("Suorakulmion pinta-ala on " + str(pinta_ala) + "cm².")
print("Suorakulmion piiri on " + str(piiri) + ".")