from flask import Flask, render_template
import json
import requests

with open("stores.json") as list_of_stores:    
    listOfStores = json.load(list_of_stores)
    listOfStoresInTuples = []
    for index in range(len(listOfStores)):
        name = listOfStores[index]['name']
        postcode = listOfStores[index]['postcode']
        listOfStoresInTuples.append((name, postcode))
    listOfStoresInTuples.sort()
    
listOfPostcodes = []
for index in range(len(listOfStoresInTuples)):
    listOfPostcodes.append(listOfStoresInTuples[index][1])
jsonListOfPostcodes = {"postcodes" : listOfPostcodes}
response = requests.post("https://api.postcodes.io/postcodes", json=jsonListOfPostcodes)
dictPostcodeDetails = json.loads(response.text)
longitudeAndLatitude = []
for index in range(len(listOfPostcodes)):
    try:
        longitude = dictPostcodeDetails['result'][index]['result']['longitude']
        latitude = dictPostcodeDetails['result'][index]['result']['latitude']
        # compute longitude and latitude of the postcodes as a list of tuples
        longitudeAndLatitude.append((longitude, latitude))
    except:
        # if no data is found from API
        longitudeAndLatitude.append((9999,9999))

app = Flask(__name__)

@app.route('/')
def render_list_of_stores():
    return render_template('render_stores.html', nameAndPostcode = listOfStoresInTuples, longitudeAndLatitude = longitudeAndLatitude)

if __name__ == '__main__':
    app.run(debug = True)   