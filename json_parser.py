import requests


def parse():
    response1 = requests.get('https://gbfs.fordgobike.com/gbfs/es/station_information.json')
    stations1 = response1.json()["data"]["stations"]

    dictStationCapacity = dict()

    for station in stations1:
        dictStationCapacity[station["station_id"]] = station["capacity"]

    response2 = requests.get('https://gbfs.fordgobike.com/gbfs/es/station_status.json')
    stations2 = response2.json()["data"]["stations"]

    result = list()

    for station in stations2:
        temp_dict = dict()
        temp_dict["last_reported"] = station["last_reported"]
        temp_dict["station_id"] = str(station["station_id"])
        temp_dict["num_ebikes_available"] = station["num_ebikes_available"]
        temp_dict["num_bikes_available"] = station["num_bikes_available"]
        temp_dict["num_docks_available"] = station["num_docks_available"]
        temp_dict["station_status"] = station["station_status"]
        temp_dict["capacity"] = dictStationCapacity[station["station_id"]]
        result.append(temp_dict)

    return result
