import json

def parseFlightList(flightData):
	print(type(flightData))
	flightJSON = json.loads(flightData)
	for flight in flightJSON:
		flight['departureTime'] = flight['departureTime'][0:10] + "   --   " + flight['departureTime'][11:16]
		print (flight)



	return flightJSON


	print(type(flightJSON))
	