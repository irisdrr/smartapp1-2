from sprint1 import weerstation
from sprint2 import smart_app_controller

def smart_app():

    while True:

        print("\n===== SMART APP =====")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Stoppen")

        keuze = input("Wat wil je gebruiken: ")

        if keuze == "1":
            weerstation()

        elif keuze == "2":
            smart_app_controller()

        elif keuze == "3":
            print("Smart App gestopt, Tot ziens!")
            break

        else:
            print("Ongeldige keuze.")

smart_app()
