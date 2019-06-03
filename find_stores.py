import json


# Open the json file and convert it into a list of dictionaries
with open("stores.json") as store_list:    
    list_of_stores = json.load(store_list)
    
    # Convert the dictionaries into tuples of (name, postcode) and
    # subsequently create a list of tuples
    list_of_stores_in_tuples = []
    for index in range(len(list_of_stores)):
        name = list_of_stores[index]['name']
        postcode = list_of_stores[index]['postcode']
        list_of_stores_in_tuples.append((name, postcode))
        
    # Sort the list of tuples in alphabetical order
    list_of_stores_in_tuples.sort()