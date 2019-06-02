from render_stores_application import listOfStoresInTuples, longitudeAndLatitude
from math import cos, asin, sqrt
import math
import requests
import json

# Function found in Stackoverflow to mathematically compute distance in kilometres between two points based on longitude and latitude 
def distance(lat1, lon1, lat2, lon2):
    p = math.pi / 180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

def list_of_stores_within_radius(postcode, radius):
    response = requests.get("https://api.postcodes.io/postcodes/" + postcode)
    postcodeDetails = json.loads(response.text)
    try:
        longitudeOfPostcode = postcodeDetails['result']['longitude']
        latitudeOfPostcode = postcodeDetails['result']['latitude']
        listOfStoresWithinRadius = []
        listOfCoordinates = []
        for index in range(len(listOfStoresInTuples)):
            longitudeOfStore = longitudeAndLatitude[index][0]
            latitudeOfStore = longitudeAndLatitude[index][1]
            distanceStoreToPostcodeInKM = distance(latitudeOfPostcode, longitudeOfPostcode, latitudeOfStore, longitudeOfStore)
            if distanceStoreToPostcodeInKM <= radius:
                listOfStoresWithinRadius.append(listOfStoresInTuples[index])
                listOfCoordinates.append(longitudeAndLatitude[index])
        lengthCoordinateList = range(len(listOfCoordinates))
        # indexes of sorted latitudes north to south (in descending order)
        sortedIndexByLatitude = sorted(lengthCoordinateList, key=lambda k: listOfCoordinates[k][1], reverse=True)
        # compute list of stores ordered from north to south
        listOfStoresNorthToSouth = []
        for index in lengthCoordinateList:
            loopThruLatitudeIndexes = sortedIndexByLatitude[index]
            listOfStoresNorthToSouth.append(listOfStoresWithinRadius[loopThruLatitudeIndexes])
        return listOfStoresNorthToSouth
    except:
        fatalMessage = 'Invalid postcode'
        return fatalMessage

print('This program returns a list of stores within a given radius of a given postcode.')
print('The stores sorted from north to south.')
testPostCode = input('Please enter a postcode: ')
testRadius = input('Please enter a radius in km: ')    
testResult = list_of_stores_within_radius(testPostCode, float(testRadius))
print(testResult)