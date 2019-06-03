from find_stores import list_of_stores_in_tuples
from find_longitude_and_latitude import longitude_and_latitude
from find_distance import distance
import requests
import json


def list_of_stores_within_radius(postcode, radius):
    
    # Request API to return data from given postcode
    response = requests.get("https://api.postcodes.io/postcodes/" + postcode)
    
    # Convert return data into dictionary
    postcode_details = json.loads(response.text)
    
    # If postcode data is returned by API
    try:
        # Extract longitude and latitude of the postcode
        longitude_of_postcode = postcode_details['result']['longitude']
        latitude_of_postcode = postcode_details['result']['latitude']
        
        list_of_stores_within_radius = []
        list_of_coordinates = []
        for index in range(len(list_of_stores_in_tuples)):
            
            # Compute longitude and latitude of each store
            longitude_of_store = longitude_and_latitude[index][0]
            latitude_of_store = longitude_and_latitude[index][1]
            
            # Compute distance from each store to given postcode
            distance_store_to_postcode = distance(latitude_of_postcode, 
                                                  longitude_of_postcode, 
                                                  latitude_of_store, 
                                                  longitude_of_store)
            
            if distance_store_to_postcode <= radius:
                
                # Append store into list if within given radius 
                list_of_stores_within_radius.append(list_of_stores_in_tuples[index])
                
                # Compute their corresponding longitude and latitude
                # (named 'coordinates' here for brevity
                list_of_coordinates.append(longitude_and_latitude[index])
        
        # Compute list of indexes of latitudes sorted in descending order 
        # (i.e. north to south)
        length_coordinate_list = range(len(list_of_coordinates))
        sorted_index_by_latitude = sorted(length_coordinate_list, 
                                          key=lambda 
                                          index: list_of_coordinates[index][1], 
                                          reverse=True)
        
        # Using the above list of indexes, compute list of stores 
        # ordered from north to south
        list_of_stores_north_to_south = []
        for index in length_coordinate_list:
            loop_thru_latitude_indexes = sorted_index_by_latitude[index]
            list_of_stores_north_to_south.append(
                    list_of_stores_within_radius[loop_thru_latitude_indexes]
                                                )
        return list_of_stores_north_to_south
    
    # If no postcode data is returned by API, i.e. postcode is invalid
    except:
        fatal_message = 'Invalid postcode'
        return fatal_message


# Test the functionality
print('This program returns a list of stores within a given radius of a '
      'given postcode. The stores are sorted from north to south.')
       
test_postCode = input('Please enter a postcode: ')
test_radius = input('Please enter a radius in km: ')    
test_result = list_of_stores_within_radius(test_postCode, float(test_radius))

print(test_result)
