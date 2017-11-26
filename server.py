from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from server_helpers import get_latlongs, get_response, add_to_HikeTrails_db, search_past_hikes, search_user_ratings, search_user_comments
import requests, json
import urllib
import os
import pdb
from model import connect_to_db, db, User, Rating, Comment, HikeTrail, Search
from sqlalchemy import and_
import datetime


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


# Home page
@app.route("/")
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/register", methods=["GET"])
def user_registration():
    """Direct to the registration page upon button click"""

    return render_template("registration_form.html")


@app.route('/user-profile/<user_name>')
def show_userprofile(user_name):
    """Show User profile on register or login"""

    # @TODO: Add if statement to check user's logged in

    session_user = User.query.filter_by(user_name=user_name).first()
    user_id = session_user.user_id

    past_searches = search_past_hikes(user_id)
    past_ratings = search_user_ratings(user_id)
    past_comments = search_user_comments(user_id)

    return render_template("user_profile.html", user_name=user_name,
                           past_searches=past_searches,
                           past_ratings=past_ratings,
                           past_comments=past_comments)


@app.route("/register", methods=["POST"])
def register_user():
    """Checks the user information, and adds to User database
    if not already existing"""

    user_name = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")

# At the registration page, check if the user_name, email and password entered,
# already exists in the database (by querying the database)
    check_user = User.query.filter_by(user_name=user_name).count()
    # import pdb; pdb.set_trace()

    if check_user == 0:
        new_user = User(user_name=user_name, email=email, password=password)
        # Adding new user to the database and commit
        db.session.add(new_user)
        db.session.commit()

        session["user_name"] = new_user.user_name
        return redirect("/user-profile/%s" % new_user.user_name)

    else:
        flash("You have an account. Please login")
        return redirect('/choose-login')


@app.route("/choose-login", methods=["GET"])
def show_loginpage():
    """Direct to the Login page upon button click"""

    return render_template("login_form.html")


@app.route("/choose-login", methods=["POST"])
def login_process():
    """Process login."""

    # Get form variables
    user_name = request.form["user_name"]
    password = request.form["password"]

    check_user = User.query.filter_by(user_name=user_name).first()

# If the password is incorrect (checking if check_user is None), go to login page again
# Checking if the above query returns an empty list of objects
    if not check_user:
        flash("No such user")
        return redirect("/choose-login")

    if check_user.password != password:
        flash("Incorrect password. Please try again!")
        return redirect('/choose-login')

    #If user exists, add user_id to the sesssion.
    flash("You were successfully logged in")
    # The user_id value (from the returned list) is added to the session dictionary
    session["user_name"] = check_user.user_name
    # user_name = session["user_name"]
    return redirect("/user-profile/%s" % user_name)


@app.route('/logout')
def logout_user():

    del session["user_name"]
    return redirect("/")


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

    city = None
    state = None
    curr_lat = 0.0
    curr_long = 0.0

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

        # search_type = "search-by-city"

    elif "/search-by-loc" in request.referrer:
        radius = request.form["radius"]
        curr_lat = request.form["curr-lat"]
        curr_long = request.form["curr-long"]

        # The payload params includes the latlong values
        payload = {"q[activities_activity_type_name_eq]": "hiking",
                   "lat": curr_lat, "lon": curr_long, "limit": 20,
                   "radius": radius}

        # search_type = "search-by-location"

    # Make API request, based on the payload values
    # Pass the payload argument to get_response function
    results = get_response(payload)
    result_list = results["places"]

    # Add results to the HikeTrails database
    add_to_HikeTrails_db(result_list)
    # Get the latlong values of all the search results
    latlong_list = get_latlongs(result_list)

    return render_template("search_results.html",
                           result_list=result_list, latlong_list=latlong_list,
                           google_map_key=google_map_key,
                           city=city, state=state, radius=radius,
                           curr_lat=curr_lat, curr_long=curr_long)


@app.route("/save-search", methods=['POST'])
def save_searches():
    """Saves search criteria by the user"""

    user_name = request.form["name"]
    # user_name = session["user_name"]
    session_user = User.query.filter_by(user_name=user_name).first()
    user_id = session_user.user_id

    city = request.form["city"]
    state = request.form["state"]
    radius = int(request.form["radius"])
    curr_lat = float(request.form["curr-lat"])
    curr_long = float(request.form["curr-long"])

    search_query = Search.query.filter_by(user_id=user_id, city=city, state=state,
                                          lat_value=curr_lat,
                                          long_value=curr_long,
                                          radius=radius).count()
    if curr_lat == 0.0:
        if search_query == 0:
            new_search = Search(user_id=user_id, city=city, state=state,
                                lat_value=curr_lat, long_value=curr_long,
                                radius=radius, searched_at=datetime.datetime.utcnow())
            db.session.add(new_search)
            db.session.commit()
            flash("Search added successfully")

    return redirect("/user-profile/%s" % user_name)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")
