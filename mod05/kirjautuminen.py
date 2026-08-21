user = "python"
password = "rules"
attempts = 0

guessed_user = input("Käyttäjänimi: ")
guessed_password = input("Salasana: ")
attempts += 1

while guessed_user != user and guessed_password != password or attempts <= 5:
    if  guessed_user == user and guessed_password == password:
        print("Tervetuloa")
        break
    elif attempts >= 5:
        print("Pääsy evätty.")
        break
    print("Yritä uudelleen")
    guessed_user = input("Käyttäjänimi: ")
    guessed_password = input("Salasana: ")
    attempts += 1
