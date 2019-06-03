from math import cos, asin, sqrt
import math



# Function found in Stackoverflow to mathematically compute distance in km 
# between two points given their longitude and latitude (Haversine formula)
def distance(latitude1, longitude1, latitude2, longitude2):
    circumference = math.pi / 180
    earth_radius = 6371
    long_equation = (0.5 - cos((latitude2 - latitude1) * circumference)/2 
         + cos(latitude1 * circumference) * cos(latitude2 * circumference) 
         * (1 - cos((longitude2 - longitude1) * circumference)) / 2)
    distance_pt1_and_pt2 = 2 * earth_radius * asin(sqrt(long_equation))
    return distance_pt1_and_pt2