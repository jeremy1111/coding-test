from flask import Flask, render_template
from models.stores_model import Stores
from models.long_and_lat_model import LongitudeAndLatitude
from models.stores_in_radius_model import StoresWithinRadius


"""The controller retrieves data from the stores and long_and_lat 
   models and renders it using the html template
   The get_stores_within_radius method retrieves data from 
   stores_in_radius_model which will be used for unit testing
   Dependencies: Stores class,
                 LongitudeAndLatitude class, 
                 StoresWithinRadius class
"""


class Controller:

    def __init__(self, stores, long_and_lat, stores_within_radius):
        """Initialize a Controller object with:
           stores - an instance of the Stores class
           long_and_lat - an instance of the LongitudeAndLatitude class
           stores_within_radius - an instance of the StoresWithinRadius class
        """
        self.stores = stores
        self.long_and_lat = long_and_lat
        self.stores_within_radius = stores_within_radius

        
    def get_stores_data(self):
        """Get the stores town and postcodes from stores_model
           Returns list of tuples (town, postcode)
        """
        towns_and_postcodes = self.stores.get_sorted_list_of_stores()
        return towns_and_postcodes

        
    def get_long_and_lat_data(self):
        """Get longitude and latitude from long_and_lat_model
           Returns list of tuples (longitude, latitude)
        """
        list_of_long_and_lat = self.long_and_lat.get_long_and_lat_list(
                            stores.get_postcodes()
        )
        return list_of_long_and_lat

    
    def get_long_and_lat_within_radius(self):
        """From stores_in_radius_model, get list of longitudes and  
           latitudes within specified radius ordered from north to south
           Takes a string (postcode) and a float (radius) as arguments
           Returns list of tuples
        """
        long_and_lat_within_radius = \
            self.stores_within_radius.get_long_and_lat_list_sorted_by_lat()
        return long_and_lat_within_radius                                          

        
    def get_stores_within_radius(self):
        """From stores_in_radius_model, get list of stores within 
           specified radius ordered from north to south
           Takes a string (postcode) and a float (radius) as arguments
           Returns list of tuples
        """                      
        stores_within_radius = \
               self.stores_within_radius.get_stores_within_radius_ordered()
        return stores_within_radius



      
"""Render"""

app = Flask(__name__)

stores = Stores()
long_and_lat = LongitudeAndLatitude()
# No need to render stores within radius, so set to None
controller = Controller(stores, long_and_lat, None)
town_and_postcodes = controller.get_stores_data()
longitude_and_latitude = controller.get_long_and_lat_data()

@app.route('/stores', methods=['GET', 'POST'])
def render_list_of_stores():
    
    return render_template('render_stores.html',
                           name_and_postcode = town_and_postcodes,
                           image = "/static/tenor.gif")

@app.route('/stores_and_long_and_lat', methods=['GET', 'POST'])
def render_list_of_stores_with_coordinates():
    
    return render_template('render_stores.html', 
                           name_and_postcode = town_and_postcodes, 
                           longitude_and_latitude = longitude_and_latitude,
                           image = "/static/tenor.gif")

if __name__ == '__main__':
    app.run(debug = True)   
        