leiviskät = input("Syötä leiviskät:")
naulat = input("Syötä naulat:")
luodit = input("Syötä luodit:")

luoti = float(13.3)
naula = 32 * luoti
leiviskä = 20 * naula

leiviskäyht = float(leiviskät) * float(leiviskä)
naulayht = float(naulat) * float(naula)
luotiyht = float(luodit) * float(luoti)

massa = leiviskäyht + naulayht + luotiyht

massakg = int(massa // 1000)
massag = massa % 1000

print(f"Massa: {massakg:} kg ja {massag:.2f} g")