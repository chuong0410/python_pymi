import requests
import json
import time

link_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
keyword = "beer"
location = "21.013111,105.799972"
radius = "2000"

def get_api():
	with open("api_googlemap.txt", "rt") as f:
		data = f.read()
	return data

def find_beer(keyword, location, radius):
	result = []
	dict_data = {"keyword" : keyword,
				 "location": location,
				 "radius": radius,
				 "key" : get_api()}
	ses = requests.Session()
	reps = ses.get(link_url, params = dict_data)
	if reps.status_code // 5 == 100:
		raise Exception("Cannot connect to server!")
	data = reps.json()
	if not data:
		raise ValueError("Not found data!")
	result.extend(data['results'])
	return result

def create_geojson(beer):
	geojson_feature =[
		{
			"type": "Feature",
    		"geometry": {
        		"type": "Point",
        		"coordinates": [float(data['geometry']['location']['lng']),
        						float(data['geometry']['location']['lat'])]},
        	"properties": {"name": data["vicinity"]},
		} for data in beer]
	geojon_result = {"type": "FeatureCollection",
       				 "features": geojson_feature}
	with open("beer_pub.geojson", "wt", encoding="utf-8") as f:
		json.dump(geojon_result, f, ensure_ascii = False, indent = 4)

def main():
	result = find_beer(keyword, location, radius)
	create_geojson(result)
	#print(result)

if __name__ == "__main__":
	main()





















