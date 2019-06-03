import json



with open("stores.json") as store_list:    
    list_of_stores = json.load(store_list)
    list_of_stores_in_tuples = []
    for index in range(len(list_of_stores)):
        name = list_of_stores[index]['name']
        postcode = list_of_stores[index]['postcode']
        list_of_stores_in_tuples.append((name, postcode))
    list_of_stores_in_tuples.sort()