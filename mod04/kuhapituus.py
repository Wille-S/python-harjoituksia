kuha_pituus = int(input("Syötä kuhan pituus senttimetrinä:"))

if kuha_pituus < 37:
    print(f"Kuha on alamittainen, {37 - kuha_pituus}cm liian lyhyt, laske se takaisin järveen.")
elif kuha_pituus >= 37:
    print("Kuha on tarpeeksi pitkä.")