import random
random_number = random.randint(1, 10)
guessed_number = int(input("Arvaa numero 1-10: "))

while guessed_number != random_number:
    if guessed_number > random_number:
        print("Liian suuri arvaus")
    elif guessed_number < random_number:
        print("Liian pieni arvaus")
    guessed_number = int(input("Arvaa numero 1-10: "))
else:
    print("Oikein!")