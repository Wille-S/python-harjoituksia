import sys
import save
import functions

while True:
    functions.main_menu()
    command = input("Valitse (1-4): ")

    if command == "1":
        functions.start_game()
    elif command == "2":
        typed_name = input("Syötä nimi: ")
        if save.save_exists_for(typed_name): # check if tallennus.json has a save for name input
            loaded_player = save.load_game(typed_name)
            functions.run_game(loaded_player)
        else:
            print("Tallennusta ei löytynyt tälle nimelle.")
            input("\nPaina enter palataksesi päävalikkoon.")
    elif command == "3":
        functions.play_guide()
    elif command == "4":
        print("Kiitos kun pelasit")
        sys.exit()
    else:
        print("Väärä syöte")