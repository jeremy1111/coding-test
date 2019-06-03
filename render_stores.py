from flask import Flask, render_template
import json
import requests



with open("stores.json") as store_list:    
    list_of_stores = json.load(store_list)
    list_of_stores_in_tuples = []
    for index in range(len(list_of_stores)):
        name = list_of_stores[index]['name']
        postcode = list_of_stores[index]['postcode']
        list_of_stores_in_tuples.append((name, postcode))
    list_of_stores_in_tuples.sort()

app = Flask(__name__)

@app.route('/')
def render_list_of_stores():
    return render_template('render_stores.html', name_and_postcode = list_of_stores_in_tuples)

if __name__ == '__main__':
    app.run(debug = True)   
