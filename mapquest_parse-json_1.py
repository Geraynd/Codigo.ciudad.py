import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "fXN4dkCjysgfteHGiZotxAFLewrdQOjh" #Replace con la clave de MapQuest

while True:
    orig = input ("ubicaion inicial: ")
    if orig == "quit" or orig == "q":
        break
    dest = input ("destino: ")
    if dest == "quit" or dest == "q":
        break
    url =main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str (json_status) + "= A succefull route call. \n")
        print("==============================================")
        print("direccion desde " + (orig) + " hacia " + (dest))
        print("direccion de viaje:  " + (json_data["route"]["formattedTime"]))
        print("kilometros       " + str ("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("==============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"] :
            print((each)["narrative"] + "(" + str(" {:.2f}".format((each["distance"])*1.61) + " km)" ))
            print("==============================================")

