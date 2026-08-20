numero_lista = []
numero = input("Anna numero, lopettaaksesi jätä tyhjäksi: ")
while numero != "":
    numero_lista.append(int(numero))
    numero = input("Anna numero, lopettaaksesi jätä tyhjäksi: ")
else:
    numero_lista.sort()
    print(numero_lista)
    