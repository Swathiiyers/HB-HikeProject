from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from server_helpers import get_latlongs, get_response
import requests
import urllib
import os
import pdb

# from model import connect_to_db, db, User, Movie, Rating

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


# Home page
@app.route("/")
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/choose-login")
def show_loginpage():
    """Direct to the Login page upon button click"""

    return render_template("login_form.html")


@app.route("/choose-search")
def show_searchpage():
    """Direct to the Hike search page upon button click"""

    return render_template("search_page.html")


@app.route("/search-by-loc")
def find_loc():
    """Go to the my location search page"""

    return render_template("find_my_location_search.html")


@app.route("/search-hike", methods=["POST"])
def search_hike():
    """Search hike by location or Latlong based upon search page,
    send API request, push results to results page"""
    google_map_key = os.environ["GOOGLE_MAPS_KEY"]

# Checking if the request is from choose-search route of find-my-loc rout
# Note that here 'request' is the form request, NOT the API requests.
    if "/choose-search" in request.referrer:
        city = request.form["city"]
        state = request.form["state"]
        radius = request.form["radius"]

        # The payload params includes the city, state and radius values
        payload = {"q[activities_activity_type_name_eq]": "hiking",
                   "q[city_cont]": city, "q[state_cont]": state,
                   "q[country_cont]": "United+States",
                   "radius": radius, "limit": 10}

    elif "/search-by-loc" in request.referrer:
        radius = request.form["radius"]
        curr_lat = request.form["curr-lat"]
        curr_long = request.form["curr-long"]

        # The payload params includes the latlong values
        payload = {"q[activities_activity_type_name_eq]": "hiking",
                   "lat": curr_lat, "lon": curr_long, "limit": 20,
                   "radius": radius}

    # Make API request, based on the payload values
    # Pass the payload argument to get_response function
    results = get_response(payload)
    result_list = results["places"]
    # Get the latlong values of all the search results
    latlong_list = get_latlongs(result_list)

    return render_template("search_results.html",
                           result_list=result_list, latlong_list=latlong_list,
                           google_map_key=google_map_key)


################################################################################
# @app.route("/register", methods=["GET"])
# def register_form():
#     """Show form for user signup."""

#     return render_template("register_form.html")

#
# @app.route("/register", methods=["POST"])
# def register_process():
#     """Process registration."""

#     # Get form variables
#     email = request.form["email"]
#     password = request.form["password"]
#     age = int(request.form["age"])
#     zipcode = request.form["zipcode"]

#     new_user = User(email=email, password=password, age=age, zipcode=zipcode)

#     db.session.add(new_user)
#     db.session.commit()

#     flash("User %s added." % email)
#     return redirect("/")


# @app.route("/login", methods=["GET"])
# def login_form():
#     """Show login form."""

#     return render_template("login_form.html")


# @app.route("/login", methods=["POST"])
# def login_process():
#     """Process login."""

#     # Get form variables
#     email = request.form["email"]
#     password = request.form["password"]

#     user = User.query.filter_by(email=email).first()

#     if not user:
#         flash("No such user")
#         return redirect("/login")

#     if user.password != password:
#         flash("Incorrect password")
#         return redirect("/login")

#     session["user_id"] = user.user_id

#     flash("Logged in")
#     return redirect("/users/%s" % user.user_id)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")
