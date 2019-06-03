from find_stores import list_of_stores_in_tuples
import json
import requests


# Compute list of postcodes from the list of stores
list_of_postcodes = []
for index in range(len(list_of_stores_in_tuples)):
    list_of_postcodes.append(list_of_stores_in_tuples[index][1])

# Make the list of postcodes into a format readable by the API
json_list_of_postcodes = {"postcodes" : list_of_postcodes}

# Make a request to the API to return data from the postcodes
response = requests.post("https://api.postcodes.io/postcodes", 
                         json=json_list_of_postcodes)

# Convert the response data into a dictionary
dict_postcode_details = json.loads(response.text)

# Compute the list of longitudes and latitudes. Each pair is a tuple
# (longitude, latitude)
longitude_and_latitude = []
for index in range(len(list_of_postcodes)):
    
    # Extract longitude and latitude of each postcode from response data
    try:
        longitude = dict_postcode_details['result'][index]['result']['longitude']
        latitude = dict_postcode_details['result'][index]['result']['latitude']
        
        # Compute longitude and latitude of the postcodes as a list of 
        # tuples
        longitude_and_latitude.append((longitude, latitude))
    
    # And if no data is found from API, just set both to 9999
    except:
        longitude_and_latitude.append((9999,9999))