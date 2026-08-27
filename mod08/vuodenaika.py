vuodenajat = "Talvi", "Kevät", "Kesä", "Syksy"

talvi_kuukaudet = 12, 1, 2
kevät_kuukaudet = 3, 4, 5
kesä_kuukaudet = 6, 7, 8

kuukausi = int(input("Syötä kuukauden numero: "))

if kuukausi in talvi_kuukaudet:
    print(vuodenajat[0])
elif kuukausi in kevät_kuukaudet:
    print(vuodenajat[1])
elif kuukausi in kesä_kuukaudet:
    print(vuodenajat[2])
else:
    print(vuodenajat[3])
