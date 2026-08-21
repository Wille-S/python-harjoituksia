numero_lista = []
numero = input("Anna numero, lopettaaksesi jätä tyhjäksi: ")
while numero != "":
    numero_lista.append(int(numero))
    numero = input("Anna numero, lopettaaksesi jätä tyhjäksi: ")
else:
    numero_lista.sort(reverse=True)
    top5 = numero_lista[:5] 
    print(top5)