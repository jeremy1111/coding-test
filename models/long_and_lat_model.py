import json
import requests

"""This class takes the list of postcodes and makes requests to the API, which
   then returns corresponding data. The longitudes and latitudes are extracted
   and put into a list of tuples
   It is used by the controller
"""




class LongitudeAndLatitude:

    def __init__(self):
        pass

    
    def get_long_and_lat(self, postcode):
        """Find longitude and latitude of a single postcode
           Returns two floats
        """
        response = requests.get("https://api.postcodes.io/postcodes/" 
                                + postcode)
        postcode_details = json.loads(response.text)
        longitude_of_postcode = postcode_details['result']['longitude']
        latitude_of_postcode = postcode_details['result']['latitude']
        return longitude_of_postcode, latitude_of_postcode


    def get_long_and_lat_list(self, list_of_postcodes):
        """Find the longitudes and latitudes of a list of postcodes
           Returns a list of tuples
        """
        # Make the list of postcodes into a format readable by the API
        json_list_of_postcodes = {"postcodes" : list_of_postcodes}

        # Make a request to the API to return data from the postcodes
        response = requests.post("https://api.postcodes.io/postcodes", 
                                 json=json_list_of_postcodes)

        # Convert the response data into a dictionary
        dict_postcode_details = json.loads(response.text)

        # Compute the list of longitudes and latitudes. Each pair is a tuple
        # (longitude, latitude)
        longitudes_and_latitudes = []
        for index in range(len(list_of_postcodes)):
            
            # Extract longitude and latitude of each postcode from response data
            try:
                longitude = \
                dict_postcode_details['result'][index]['result']['longitude']
                latitude = \
                dict_postcode_details['result'][index]['result']['latitude']
                
                # Compute longitude and latitude of the postcodes as a list of 
                # tuples
                longitudes_and_latitudes.append((longitude, latitude))
            
            # And if no data is found from API, set both to 9999
            except:
                longitudes_and_latitudes.append((9999,9999))
        return longitudes_and_latitudes