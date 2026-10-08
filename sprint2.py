# SMART APP CONTROLLER - SPRINT 2


def aantal_dagen(inputFile):

    with open(inputFile, "r") as bestand:
        regels = bestand.readlines()

    return len(regels) - 1


def auto_bereken(inputFile, outputFile):

    with open(inputFile, "r") as bestand:
        regels = bestand.readlines()

    with open(outputFile, "w") as uitvoer:

        for regel in regels[1:]:

            gegevens = regel.split()

            datum = gegevens[0]
            aantal_personen = int(gegevens[1])
            setpoint = float(gegevens[2])
            buitentemp = float(gegevens[3])
            neerslag = float(gegevens[4])

            verschil = setpoint - buitentemp

            # CV-ketel
            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            # Ventilatie
            ventilatie = aantal_personen + 1

            if ventilatie > 4:
                ventilatie = 4

            # Bewatering
            if neerslag < 3:
                bewatering = True
            else:
                bewatering = False

            uitvoer.write(
                f"{datum};{cv};{ventilatie};{bewatering}\n"
            )

    print("Outputbestand aangemaakt.")


def overwrite_settings(outputFile):

    datum = input("Voer een datum in: ")

    systeem = input(
        "Kies systeem (1=CV ketel, 2=Ventilatie, 3=Bewatering): "
    )

    with open(outputFile, "r") as bestand:
        regels = bestand.readlines()

    gevonden = False

    for i in range(len(regels)):

        gegevens = regels[i].strip().split(";")

        if gegevens[0] == datum:

            gevonden = True

            nieuwe_waarde = input("Nieuwe waarde: ")

            if systeem == "1":

                waarde = int(nieuwe_waarde)

                if waarde < 0 or waarde > 100:
                    return -3

                gegevens[1] = str(waarde)

            elif systeem == "2":

                waarde = int(nieuwe_waarde)

                if waarde < 0 or waarde > 4:
                    return -3

                gegevens[2] = str(waarde)

            elif systeem == "3":

                if nieuwe_waarde == "0":
                    gegevens[3] = "False"

                elif nieuwe_waarde == "1":
                    gegevens[3] = "True"

                else:
                    return -3

            else:
                return -3

            regels[i] = ";".join(gegevens) + "\n"

            break

    if not gevonden:
        return -1

    with open(outputFile, "w") as bestand:
        bestand.writelines(regels)

    return 0


def smart_app_controller():

    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:

        print("\nSMART APP CONTROLLER")
        print("1. Hoeveel dagen zijn er aanwezig?")
        print("2. Automatisch alle actuatoren berekenen")
        print("3. Een waarde overschrijven")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":

            print(
                "Aantal dagen aanwezig:",
                aantal_dagen(inputFile)
            )

        elif keuze == "2":

            auto_bereken(
                inputFile,
                outputFile
            )

        elif keuze == "3":

            resultaat = overwrite_settings(
                outputFile
            )

            if resultaat == 0:
                print("Waarde succesvol aangepast.")

            elif resultaat == -1:
                print("Datum niet gevonden.")

            elif resultaat == -3:
                print("Ongeldige invoer.")

        elif keuze == "4":

            print("Programma afgesloten.")
            break

        else:

            print("Ongeldige keuze.")


