from flask import Flask, render_template
from find_stores import list_of_stores_in_tuples
from find_longitude_and_latitude import longitude_and_latitude


app = Flask(__name__)

@app.route('/stores')
def render_list_of_stores():
    return render_template('render_stores.html', 
                           name_and_postcode = list_of_stores_in_tuples)

@app.route('/stores_and_coordinates')
def render_list_of_stores_with_coordinates():
    return render_template('render_stores_with_long_and_lat.html', 
                           name_and_postcode = list_of_stores_in_tuples, 
                           longitude_and_latitude = longitude_and_latitude)

if __name__ == '__main__':
    app.run(debug = True)   