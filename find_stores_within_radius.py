from render_stores import listOfStoresInTuples
from render_longitude_and_latitude import longitudeAndLatitude
from find_distance import distance
import requests
import json



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