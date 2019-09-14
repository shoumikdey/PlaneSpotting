from planespotting import utils

def get_all_station_data():
    data = utils.load_json("planespotting/gs_data.json")
    print(data)
