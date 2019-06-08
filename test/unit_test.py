import sys
import os
import unittest
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root + '/models')
sys.path.append(root + '/helper_functions')
sys.path.append(root)
from stores_model import Stores
from long_and_lat_model import LongitudeAndLatitude
from stores_in_radius_model import StoresWithinRadius
from controller import Controller
from find_distance import distance


"""Test that the stores_in_radius_model finds the correct stores within
   a specified radius
"""

class Test(unittest.TestCase):

    def test(self):
    
        # Define test postcode and test radius
        postcode = 'EC1N 2HT'
        radius = 15
        
        # Create instances of objects
        stores = Stores()
        long_and_lat = LongitudeAndLatitude()
        stores_within_radius = StoresWithinRadius(postcode, radius)
        controller = Controller(stores, long_and_lat, stores_within_radius)
        
        # List of sorted longitude and latitude of stores within
        # test radius
        long_and_lat_within_radius = \
                controller.get_long_and_lat_within_radius()
                
        # List of longitude and latitude of stores not within
        # test radius
        long_and_lat_all = controller.get_long_and_lat_data()
        long_and_lat_outside_radius = []
        for i in range(len(long_and_lat_all)):
            if long_and_lat_all[i] not in long_and_lat_within_radius:
                long_and_lat_outside_radius.append(long_and_lat_all[i])
        
        # Longitude and latitude of test postcode
        long_and_lat_of_postcode = long_and_lat.get_long_and_lat([postcode])
        longitude_of_postcode = long_and_lat_of_postcode[0][0]
        latitude_of_postcode = long_and_lat_of_postcode[0][1]
        
        # Test if stores within radius are really within radius
        for i in range(len(long_and_lat_within_radius)):
            longitude_of_store = long_and_lat_within_radius[i][0]
            latitude_of_store = long_and_lat_within_radius[i][1]
            distance_postcode_to_store = distance(latitude_of_postcode,
                                                  longitude_of_postcode,
                                                  latitude_of_store,
                                                  longitude_of_store)
            self.assertTrue(distance_postcode_to_store <= radius)
        
        # Test if stores outside radius are really outside radius
        for i in range(len(long_and_lat_outside_radius)):
            longitude_of_store = long_and_lat_outside_radius[i][0]
            latitude_of_store = long_and_lat_outside_radius[i][1]
            distance_postcode_to_store = distance(latitude_of_postcode,
                                                  longitude_of_postcode,
                                                  latitude_of_store,
                                                  longitude_of_store)
            self.assertTrue(distance_postcode_to_store > radius)
            
        # Test if stores within radius are really ordered north to south
        # i.e. if latitudes are in descending order
        for i in range(len(long_and_lat_within_radius) - 1):
            self.assertTrue(long_and_lat_within_radius[i + 1][1] \
                            < long_and_lat_within_radius[i][1])

        
if __name__ == '__main__':
    unittest.main()