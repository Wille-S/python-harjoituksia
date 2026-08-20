vuosiluku = int(input("Syötä vuosiluku:"))

vuosiluku_jaettuna_sadalla = vuosiluku % 100
vuosiluku_jaettuna_neljällä = vuosiluku % 4
vuosiluku_jaettuna_neljällä_sadalla = vuosiluku % 400

if vuosiluku_jaettuna_neljällä == 0:
    if vuosiluku_jaettuna_sadalla == 0:
        if vuosiluku_jaettuna_neljällä_sadalla == 0:
            print("On karkausvuosi")
        else:
            print("Ei ole karkausvuosi")
    else:
        print("On karkausvuosi")
else:
    print("Ei ole karkausvuosi")