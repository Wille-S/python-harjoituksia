class Hissi:
    def __init__(self, alin, ylin):
        self.kerros = alin
        self.alin = alin
        self.ylin = ylin        

    def siirry_kerrokseen(self, k):
        if k < self.kerros:
            kerrat = self.kerros - k
            for i in range(kerrat):
                self.kerros_alas()
        elif k > self.kerros:
            kerrat = k - self.kerros
            for i in range(kerrat):
                self.kerros_ylös()            

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin, ylin, hissien_lukumäärä,):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for _ in range(hissien_lukumäärä):
            self.hissit.append(Hissi(alin, ylin))


    def aja_hissiä(self, h, k):
        print(f"Hissi {h} ajaa nyt kerrokseen {k}")
        self.hissit[h - 1].siirry_kerrokseen(k)

    def palohälytys(self):
        print("Hissit ajavat nyt pohjakerrokseen.")
        for numero in range(1, len(self.hissit) + 1):
            self.aja_hissiä(numero, self.alin)

#h = Hissi(1, 10)

h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 4)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 2)

talo.palohälytys()


#print(f"Kerros nyt {h.kerros}")

#h.siirry_kerrokseen(5)
#print(f"Kerros nyt {h.kerros}")

#h.siirry_kerrokseen(1)
#print(f"Kerros nyt {h.kerros}")