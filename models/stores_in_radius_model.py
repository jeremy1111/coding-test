import requests
import json
import os
import sys
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root + '/helper_functions')
from models.stores_model import Stores
from models.long_and_lat_model import LongitudeAndLatitude
from find_distance import distance


"""This class takes the longitude and latitude from a postcode and a radius 
   to find stores within said radius
   It is used by the controller 
   Inherits from: Stores class, 
                  LongitudeAndLatitude class
"""



class StoresWithinRadius(Stores, LongitudeAndLatitude):

    def __init__(self, postcode, radius):
        super().__init__() 
        self.postcode = postcode
        self.radius = radius


    def _get_list_of_long_and_lat(self):
        """Compute list of longitude and latitude of stores within radius
        """
        # Compute list of names and postcodes of all stores
        list_of_stores = self.get_sorted_list_of_stores()
        
        # Compute list of longitudes and latitudes of all stores
        longitudes_and_latitudes = \
                self.get_long_and_lat_list(self.get_postcodes())
        
        self.list_of_stores_within_radius = []
        list_of_long_and_lat = []
        
        for item in longitudes_and_latitudes:
            
            # Compute longitude and latitude of each store
            longitude_of_store = item[0]
            latitude_of_store = item[1]
            
            # Compute distance from each store to given postcode
            (longitude_of_postcode, 
             latitude_of_postcode) = self.get_long_and_lat(self.postcode)
                                            
            distance_store_to_postcode = distance(latitude_of_postcode, 
                                                  longitude_of_postcode, 
                                                  latitude_of_store, 
                                                  longitude_of_store)
            
            if distance_store_to_postcode <= self.radius:
                
                # Append store into list if within given radius
                index = longitudes_and_latitudes.index(item)
                self.list_of_stores_within_radius.append(list_of_stores[index])
                
                # Compute their corresponding longitude and latitude
                list_of_long_and_lat.append(item)       
        return list_of_long_and_lat

        
    def _get_sorted_list_of_indexes_by_lat(self):
        """Compute list of indexes of latitudes sorted in descending order 
        (i.e. north to south)
        """
        list_of_long_and_lat = self._get_list_of_long_and_lat()
        self.len_of_long_and_lat_list = range(len(list_of_long_and_lat))
        
        sorted_indexes_list_by_latitude = sorted(
                                      self.len_of_long_and_lat_list, 
                                      key=lambda 
                                      index: list_of_long_and_lat[index][1], 
                                      reverse=True
        )
        return sorted_indexes_list_by_latitude
 
 
    def get_stores_within_radius_ordered(self):
        """Using the list of indexes sorted by latitude, compute list of stores 
           ordered from north to south
        """
        try:
            # If postcode data is returned by API
            sorted_indexes_list_by_latitude = self._get_sorted_list_of_indexes_by_lat()
            list_of_stores_north_to_south = []
            for index in self.len_of_long_and_lat_list:
                loop_thru_latitude_indexes = sorted_indexes_list_by_latitude[index]
                list_of_stores_north_to_south.append(
                        self.list_of_stores_within_radius[loop_thru_latitude_indexes]
                )
            return list_of_stores_north_to_south        
        except:
            # If no postcode data is returned by API
            return 'Invalid postcode'
            

    def get_long_and_lat_list_sorted_by_lat(self):
        """Compute list of longitudes and latitudes sorted by latitude in 
           descending order (north to south)
        """
        list_of_long_and_lat = self._get_list_of_long_and_lat()
        list_of_long_and_lat.sort(key = lambda item: item[1], reverse = True)
        return list_of_long_and_lat