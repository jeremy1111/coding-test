import json
import os

"""This class inputs the json file and converts the data into a list of 
   tuples. It is used by the controller
"""



class Stores:

    def __init__(self):
        """Open the json file and convert it into a list of dictionaries
        """
        root = os.path.join(os.path.dirname(__file__), '..')
        with open(root + "\static\stores.json") as store_list:    
            self.list_of_stores = json.load(store_list)

       
    def get_sorted_list_of_stores(self):
        """Convert the dictionaries into tuples of (name, postcode) and
           subsequently create a list of tuples (name, postcode)
        """
        list_of_stores_in_tuples = []
        for item in self.list_of_stores:
            name = item['name']
            postcode = item['postcode']
            list_of_stores_in_tuples.append((name, postcode))
            
        # Sort the list of tuples with names in alphabetical order
        list_of_stores_in_tuples.sort()
        return list_of_stores_in_tuples

        
    def get_postcodes(self):
        """Get the list of postcodes
           Returns list of strings ['postcode1', 'postcode2', ...]
        """
        list_of_postcodes = []
        for item in self.get_sorted_list_of_stores():
            list_of_postcodes.append(item[1])
        return list_of_postcodes