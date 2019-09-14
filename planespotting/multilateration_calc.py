from planespotting import utils

def get_all_station_data():
    data = utils.load_json("planespotting/gs_data.json")
    known_st = []
    for i in data:
        known_st.append([data[i]['lat'], data[i]['lon'], data[i]['alt']])
