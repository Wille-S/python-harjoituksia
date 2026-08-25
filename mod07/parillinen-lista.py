lista = [5, 7, 3, 20, 6, 12]

def parillinen_lista (l):
    p_lista = []
    for i in l:
        if i % 2 == 0:
            p_lista.append(i)
    return p_lista

print("Alkuperäinen lista: " + str(lista))
print("Lista vain parillisilla luvuilla: " + str(parillinen_lista(lista)))