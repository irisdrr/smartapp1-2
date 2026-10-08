import requests


def huidig_weer():
    try:
        stad = input("Voer een stad in: ").strip()

    except (EOFError, KeyboardInterrupt):
        print("\nHuidig weer gestopt.")
        return

    if stad == "":
        print("Je moet een stad invoeren.")
        return

    geocoding_url = (
        "https://geocoding-api.open-meteo.com/v1/search"
    )

    geocoding_params = {
        "name": stad,
        "count": 1,
        "language": "nl"
    }

    try:
        locatie_response = requests.get(
            geocoding_url,
            params=geocoding_params,
            timeout=10
        )

        locatie_response.raise_for_status()

        locatie_data = locatie_response.json()

        if not locatie_data.get("results"):
            print("Stad niet gevonden.")
            return

        locatie = locatie_data["results"][0]

        latitude = locatie["latitude"]
        longitude = locatie["longitude"]
        plaatsnaam = locatie["name"]

        weer_url = (
            "https://api.open-meteo.com/v1/forecast"
        )

        weer_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m"
        }

        weer_response = requests.get(
            weer_url,
            params=weer_params,
            timeout=10
        )

        weer_response.raise_for_status()

        weer_data = weer_response.json()

        temperatuur = weer_data[
            "current"
        ]["temperature_2m"]

        print()
        print(
            f"De huidige temperatuur in "
            f"{plaatsnaam} is {temperatuur}°C"
        )

    except requests.Timeout:
        print(
            "Fout: het ophalen van het weer duurde te lang."
        )

    except requests.ConnectionError:
        print(
            "Fout: geen verbinding met internet."
        )

    except requests.RequestException:
        print(
            "Fout: het weer kon niet worden opgehaald."
        )

    except (KeyError, IndexError, TypeError):
        print(
            "Fout: de ontvangen weergegevens zijn ongeldig."
        )

    except ValueError:
        print(
            "Fout: de ontvangen gegevens konden niet worden gelezen."
        )