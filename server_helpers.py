from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Review, HikeTrail, Search
import requests
import urllib
import os


# Helper function that makes API requests based on the payload parameter
def get_response(payload):
    """Takes payload as parameter and returns the jsonified response from
    the TrailAPI"""

    base_url = "https://trailapi-trailapi.p.mashape.com/?"

    # Encoding payload values for adding it to the URL
    # Using urllib to encode params to URL, replace encoded characters to the URL compatible chars
    param_url = urllib.urlencode(payload).replace('%5D', ']').replace('%5B', '[').replace('%2B', '+')

    # Prints the param_url on terminal window for testing purpose
    print param_url

    # Concatenating base_url with final_url, to get the final_url to pass to API request.get
    final_url = base_url + param_url
    my_key = os.environ["X_MASHAPE_KEY"]
    headers = {"X-Mashape-Key": my_key, "Accept": "text/plain"}

    # Making the API call, by passing the request URL and API keys (in headers)
    response = requests.get(final_url, headers=headers)
    results = response.json()
    return results


def add_to_HikeTrails_db(result_list):

    for i in range(len(result_list)):
        trail_id = result_list[i]["unique_id"]
        trail_name = result_list[i]["name"]
        trail_description = result_list[i]["activities"][0]["description"]
        trail_length = result_list[i]["activities"][0]["length"]
        trail_directions = result_list[i]["directions"]

        check_trail = HikeTrail.query.filter_by(trail_id=trail_id).count()

        if check_trail == 0:
            new_trail = HikeTrail(trail_id=trail_id, trail_name=trail_name,
                                  trail_description=trail_description,
                                  trail_length=trail_length,
                                  trail_directions=trail_directions)
            # Adding new user to the database and commit
            db.session.add(new_trail)
    db.session.commit()


# Helper function for the '/search-hike route
# Takes the list of jsonified dict, and returns the list of latlong values
def get_latlongs(result_list):
    """Get the jsonified response from the app view, return list of latlongs"""
    # Initializing list of Latlong values
    latlong_list = []

    # Dictionary of latlong value, for each latlong pair (from search results)
    d = {}

    # For loop to append each latlong pair to the list of latlong dict (d)
    for i in range(len(result_list)):

        d['latlong'] = {'lat': result_list[i]["lat"], 'lng': result_list[i]["lon"]}

        # Adding trail information, to be able to pass to map info Window and div elements
        d['trail_id'] = result_list[i]["unique_id"]
        d['trail_name'] = result_list[i]["name"]

        # appending the latlong values and trail information to the dictionary
        latlong_list.append(d)
        # The dictionary is made empty again, to avoid over-writing same
        # dict values, all over the list.
        d = {}
    return latlong_list


# Function to check User's saved searches
def search_past_hikes(user_id):
    """Take the user_id from server, query database and return all the searches
    that user has saved"""

    past_searches = Search.query.filter_by(user_id=user_id).all()

    return past_searches
