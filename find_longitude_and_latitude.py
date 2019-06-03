from find_stores import list_of_stores_in_tuples
import json
import requests



list_of_postcodes = []
for index in range(len(list_of_stores_in_tuples)):
    list_of_postcodes.append(list_of_stores_in_tuples[index][1])
json_list_of_postcodes = {"postcodes" : list_of_postcodes}
response = requests.post("https://api.postcodes.io/postcodes", json=json_list_of_postcodes)
dict_postcode_details = json.loads(response.text)
longitude_and_latitude = []
for index in range(len(list_of_postcodes)):
    try:
        longitude = dict_postcode_details['result'][index]['result']['longitude']
        latitude = dict_postcode_details['result'][index]['result']['latitude']
        # compute longitude and latitude of the postcodes as a list of tuples
        longitude_and_latitude.append((longitude, latitude))
    except:
        # if no data is found from API, set both to 9999
        longitude_and_latitude.append((9999,9999))