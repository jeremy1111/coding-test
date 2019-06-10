## Requirements
> Assumed to be running on Windows 10 and that pip is already installed
>
> Python 3 is required

## How to run the code
> Extract everything from the zip file into a directory of your choice
>
> Open a command prompt and go into the directory
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
