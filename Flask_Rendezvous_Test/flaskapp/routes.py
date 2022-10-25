""" routes.py - Flask route definitions

Flask requires routes to be defined to know what data to provide for a given
URL. The routes provided are relative to the base hostname of the website, and
must begin with a slash."""
from flaskapp import app
from flask import render_template, jsonify
from flask import request
from wrangling_scripts.wrangling import data_wrangling, username, rating_wrangling, get_actor

header, table = data_wrangling()

data = rating_wrangling()

# The following two lines define two routes for the Flask app, one for just
# '/', which is the default route for a host, and one for '/index', which is
# a common name for the main page of a site.
#
# Both of these routes provide the exact same data - that is, whatever is
# produced by calling `index()` below.
@app.route('/')
@app.route('/index')
def index():
    """Renders the index.html template"""
    # Renders the template (see the index.html template file for details). The
    # additional defines at the end (table, header, username) are the variables
    # handed to Jinja while it is processing the template.
    return render_template('index.html', table=table, header=header,
                           username=username())

@app.route('/get_data')
def get_data():
    
   actor = request.args.get('actor')
   
   places = get_actor(actor)[0:5]
   
   # example = list()
   # example.append(place1)
   # example.append(place2)
   # example.append(place1)
   # example.append(place2)
   return jsonify(places)