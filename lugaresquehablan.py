import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
while True:
    orig = input("Ubicacion Inicial: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destino: ")
    if dest == "quit" or dest == "q":
        break

    key = "fXN4dkCjysgfteHGiZotxAFLewrdQOjh"
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + "= Una llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direcion desde " + orig + " hasta " + dest)
        print("Direccion de viaje: " + json_data["route"]["formattedTime"])
        print("Millas: " + str(json_data["route"]["distance"]))
        print("Kilometros: " + str(json_data["route"]["distance"] * 1.61))

        # Obtener la duración del viaje en horas, minutos y segundos
        duration_seconds = json_data["route"]["time"]
        hours = duration_seconds // 3600
        minutes = (duration_seconds % 3600) // 60
        seconds = duration_seconds % 60
        print("Duración del viaje: {} horas, {} minutos, {} segundos".format(hours, minutes, seconds))

        # Comprobar si la información del combustible está disponible
        if "fuelUsed" in json_data["route"]:
            fuel_used = json_data["route"]["fuelUsed"]
            fuel_liters = fuel_used * 3.78541
            print("Combustible requerido: {:.2f} litros".format(fuel_liters))
        else:
            print("Información de combustible no disponible para esta ruta.")

    print("=============================================")

    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print(each["narrative"] + " (" + str("{:.2f}".format(each["distance"] * 1.61)) + " km)")
        print("=============================================\n")
