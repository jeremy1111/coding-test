# Coding challenge (Python/Flask)
## Task specification
* Create a new Python-based application with Flask
>
* Render the list of stores from the stores.json file in alphabetical order through a backend template
> 
* Use postcodes.io to get the latitude and longitude for each postcode and render them next to each store location in the template
> 
* Build the functionality that allows you to return a list of stores in any given radius of any given postcode in the UK ordered from north to south and unit test it - no need to render anything

## System requirements
> Assumed to be running on Windows 10 and that pip is already installed
>
> Python 3 is required

## How to run the code
>
> Open a command prompt and go into the directory where this package has been placed
>
> Create a virtual environment
> ```bash
> python -m venv env
> ```
>
> Activate the virtual environment
> ```bash
> env\Scripts\activate
> ```
>
> Install the requirements
> ```bash
> pip install -r requirements.txt
> ```
> 
> To run the controller to render the tables
> ```bash
> python controller.py
> ```
> Open a browser and go to the local host shown on the last line
>
> At the end of localhost:5000, type either '/stores' to show the list of stores in alphabetical order or '/stores_and_long_and_lat' to also show the longitudes and latitudes next to each store
>
> To find stores within a specified radius of a postcode, type 'python' in the command prompt to go into interactive mode
>
> Then type
> ```bash
> >>>from models.stores_in_radius_model import StoresWithinRadius
> >>>stores_within_radius = StoresWithinRadius('postcode', radius)
> >>>stores_within_radius.get_stores_within_radius_ordered()
> ```
> (Where 'postcode' is a postcode string and radius is a real number in km)
>
> To run the unit test
> ```bash
> cd test
> python unit_test.py
> ```
## What would I have changed if I had more time?

Currently, the get_long_and_lat_list() method in the LongitudeAndLatitude class returns a value of 9999 for both longitude and latitude if the API returns that the postcode is invalid. This is probably not the best way to handle an error like this. With more time I would have built a functionality to separate the 'good' postcodes from the invalid ones, and put them into separate lists and only check from the list of valid ones when using the StoresWithinRadius class.
There is also some repeated code in the unit_test.py module, namely the two for loops for testing distance from postcode to store. This is in violation of the DRY principle and I would have created a function to address this.
