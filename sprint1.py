# SMART APP SPRINT 1: WEERSTATION


# Celsius naar Fahrenheit
def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


# Gevoelstemperatuur berekenen
def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - (luchtvochtigheid / 100) * windsnelheid


# Weerrapport bepalen
def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):

    gevoel = gevoelstemperatuur(
        temp_celcius,
        windsnelheid,
        luchtvochtigheid
    )

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"

    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    elif gevoel >= 0 and gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"

    elif gevoel >= 0 and gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif gevoel >= 10 and gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."

    else:
        return "Warm! Airco aan!"


# Hoofdfunctie
def weerstation():

    temperaturen = []

    for dag in range(1, 8):

        temp_input = input(
            f"Wat is op dag {dag} de temperatuur"
        )

        if temp_input == "":
            print("bye")
            break

        try:
            temperatuur = float(temp_input)

            if temperatuur < -50 or temperatuur > 50:
                print("Ongeldige temperatuur.")
                continue

            windsnelheid_input = input(
                f"Wat is op dag {dag} de windsnelheid[m/s]: "
            )

            if windsnelheid_input == "":
                print("bye")
                break

            windsnelheid = float(windsnelheid_input)

            luchtvochtigheid_input = input(
                f"Wat is op dag {dag} de vochtigheid[%]: "
            )

            if luchtvochtigheid_input == "":
                print("bye")
                break

            luchtvochtigheid = int(
                luchtvochtigheid_input
            )

            if luchtvochtigheid < 0 or luchtvochtigheid > 100:
                print(
                    "Ongeldige vochtigheid. Voer een waarde van 0 t/m 100 in."
                )
                continue

        except ValueError:
            print(
                "Ongeldige invoer. Voer een getal in."
            )
            continue

        temperaturen.append(temperatuur)

        fahrenheit = Fahrenheit(
            temperatuur
        )

        rapport = weerrapport(
            temperatuur,
            windsnelheid,
            luchtvochtigheid
        )

        gemiddelde = (
            sum(temperaturen)
            / len(temperaturen)
        )

        print(
            f"Het is {temperatuur}C ({fahrenheit}F)"
        )
        print(rapport)
        print(
            f"Gem. temp tot nu toe is {gemiddelde}"
        )
        print("======================================")


