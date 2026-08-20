while True:
    try:
        a = int(input("Kokonaisnumero 1:"))
        b = int(input("Kokonaisnumero 2:"))
        c = int(input("Kokonaisnumero 3:"))
        break
    except ValueError:
        print("Tämä ei ole kokonaisnumero, yritä uudelleen.")

summa = a + b + c
tulo = a * b * c
ka = summa / 3

print("Summa: " + str(summa))
print("Tulo: " + str(tulo))
print("Keskiarvo: " + str(ka))