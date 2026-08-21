numero_lista = []
numero = input("Anna numero, lopettaaksesi jätä tyhjäksi: ")
while numero != "":
    numero_lista.append(int(numero))
    numero = input("Anna numero, lopettaaksesi jätä tyhjäksi: ")
else:
    numero_lista.sort()
    print("Isoin numero: " + str(max(numero_lista)) + " ja pienin numero: " + str(min(numero_lista)))
    