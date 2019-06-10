# Tails coding test

## Task completed
> Backend task with Flask 

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

## What would you have changed if you had more time?

Currently, the get_long_and_lat_list() method in the LongitudeAndLatitude class returns a value of 9999 for both longitude and latitude if the API returns that the postcode is invalid. This is probably not the best way to handle an error like this. With more time I would have built a functionality to separate the 'good' postcodes from the invalid ones, and put them into separate lists and only check from the list of valid ones when using the StoresWithinRadius class.
There is also some repeated code in the unit_test.py module, namely the two for loops for testing distance from postcode to store. This is in violation of the DRY principle and I would have created a function to address this.

## What bits did you find the toughest? What bit are you most proud of? In both cases, why?

As a relatively junior developer with limited experience in software architecture, I found it tough to determine what constitutes a 'good' architecture. Learning Flask from scratch by following online tutorials (I limited myself to short ones due to time constraints) only taught me the basics of Flask, but did not really teach me good code structuring. I had to look through a lot of github examples to make a final judgement as to how to structure my code, as getting it wrong from the start can lead to a lot of wasted time down the line.

I am proud of the fact that, having no previous knowledge of Flask and only limited experience in web development, I managed to make the application well structured, and the fact that it works! This test was a real challenge for me and I had a lot of fun along the way, by constantly learning and doing.

## How can we improve this test?

Overall I am happy with the layout of the test. If I really had to make a suggestion, perhaps a few pointers on how to determine the distance between two points based on longitudes and latitudes could have been given, as it can be hard to tell if what's found on the internet are correct, and really digging into the maths and writing it from scratch would not be straightforward.
