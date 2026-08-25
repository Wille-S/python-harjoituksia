import random
def noppa_heitto():
    global noppa 
    noppa = random.randint(1, 6)

while True:
    noppa_heitto()
    if noppa == 6:
        print(str(noppa))
        break
    else:
        print(str(noppa))