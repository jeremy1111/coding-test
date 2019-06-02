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

app = Flask(__name__)

@app.route('/')
def render_list_of_stores():
    return render_template('render_stores.html', nameAndPostcode = listOfStoresInTuples)

if __name__ == '__main__':
    app.run(debug = True)   