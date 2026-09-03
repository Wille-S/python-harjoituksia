class Hissi:
    def __init__(self, alin, ylin, kerros = 1):
        self.kerros = kerros
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

    def kerros_alas(self):
        self.kerros -= 1

class Talo:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

    def aja_hissiä(self, h, k):
        pass

h = Hissi(1, 10)

print(f"Kerros nyt {h.kerros}")

h.siirry_kerrokseen(5)
print(f"Kerros nyt {h.kerros}")

h.siirry_kerrokseen(1)
print(f"Kerros nyt {h.kerros}")