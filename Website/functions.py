import json
import requests

def parseFlightList(flightData):
	print(type(flightData))
	flightJSON = json.loads(flightData)
	for flight in flightJSON:
		# flight['departureTime'] = flight['departureTime'][0:10] + "   --   " + flight['departureTime'][11:16]
		print (flight)



	return flightJSON


	print(type(flightJSON))


def flightIdAndDateToCoordinates(flightID,date):

	URL = "http://localhost:3030/flight?flightNumber=" + flightID + "&date=" + date
	r = requests.get(URL)
	json1 = json.loads(r.content)
	print("JSON ")
	print(type(json1))
	print(json1)
	code = json1["destination"]
	URL2 = "http://localhost:3030/airports?code=" + code
	r2 = requests.get(URL2)
	print(r2.content)
	print(type(r2.content))
	json2 = json.loads(r2.content)
	print(type(json2))
	json3 = json2[0]
	print(type(json3))
	print(json3)



	

	
	# json4 = json.loads(json3)
	#json4 = json.dumps(json3)
	

	lat = json3["latitude"]
 	lon = json3["longitude"]

	return {'latitude':str(lat), 'longitude':str(lon)}