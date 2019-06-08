class PostcodesWithinRadius(object):
	
	def __init__(self, postcode, radius):
	
		self.postcode = postcode
		self.radius = radius
		
	
	def _convert_postcode_into_dict(self):
		
		# Request API to return data from given postcode
		response = requests.get("https://api.postcodes.io/postcodes/" + self.postcode)
    
		# Convert return data into dictionary
		postcode_details = json.loads(response.text)
		return postcode_details
		
	
	def get_long_and_lat_of_postcode(self):
		
		# Extract longitude and latitude of the postcode
		postcode_details = self._convert_postcode_into_dict()
		longitude_of_postcode = postcode_details['result']['longitude']
		latitude_of_postcode = postcode_details['result']['latitude']
		return longitude_of_postcode, longitude_of_postcode
	
	
	def _get_list_of_long_and_lat(self):
		"""Compute list of longitude and latitude of stores within radius
		"""
		list_of_stores_within_radius = []
        list_of_long_and_lat = []
        for index in range(len(list_of_stores_in_tuples)):
            
            # Compute longitude and latitude of each store
            longitude_of_store = longitude_and_latitude[index][0]
            latitude_of_store = longitude_and_latitude[index][1]
            
            # Compute distance from each store to given postcode
			(longitude_of_postcode, 
			 latitude_of_postcode = self._get_long_and_lat_of_postcode())
											
            distance_store_to_postcode = distance(latitude_of_postcode, 
                                                  longitude_of_postcode, 
                                                  latitude_of_store, 
                                                  longitude_of_store)
            
            if distance_store_to_postcode <= radius:
                
                # Append store into list if within given radius 
                list_of_stores_within_radius.append(list_of_stores_in_tuples[index])
                
                # Compute their corresponding longitude and latitude
                list_of_long_and_lat.append(longitude_and_latitude[index])
		
		return list_of_long_and_lat
		
	
	def _get_sorted_list_of_indexes_by_lat(self):
		
		# Compute list of indexes of latitudes sorted in descending order 
        # (i.e. north to south)
		list_of_long_and_lat = self._get_list_of_long_and_lat()
        len_of_long_and_lat_list = range(len(list_of_long_and_lat))
		
        sorted_indexes_list_by_latitude = sorted(len_of_long_and_lat_list, 
                                          key=lambda 
                                          index: list_of_long_and_lat[index][1], 
                                          reverse=True)
										  
		return sorted_indexes_list_by_latitude
	
	
	def get_long_and_lat_list_sorted_by_lat(self):
		"""Compute list of longitudes and latitudes sorted by latitude in 
		   descending order (north to south)
		"""
		list_of_long_and_lat = self._get_list_of_long_and_lat()
		sorted_list_of_long_and_lat.sort(key = lambda item: item[1], reverse = True)
		
		return sorted_list_of_long_and_lat
										  
	
	def get_stores_within_radius_ordered(self):
		"""Using the list of indexes sorted by latitude, compute list of stores 
           ordered from north to south
		"""
		try:
			# If postcode data is returned by API
			sorted_indexes_list_by_latitude = self.get_sorted_list_of_indexes_by_lat()
			list_of_stores_north_to_south = []
			for index in len_of_long_and_lat_list:
				loop_thru_latitude_indexes = sorted_indexes_list_by_latitude[index]
				list_of_stores_north_to_south.append(
						list_of_stores_within_radius[loop_thru_latitude_indexes]
													)
			return list_of_stores_north_to_south
		
		except:
			# If no postcode data is returned by API
			return 'Invalid postcode'
