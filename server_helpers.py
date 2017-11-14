from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
import urllib
import os


# Helper function for the '/search-hike route
# Takes the form inputs, and returns the jsonified data
def get_address(city, radius, state):
    """Get inputs from the search page, return json data to the calling function"""

    base_url = "https://trailapi-trailapi.p.mashape.com/?"

    # params values for the request object
    payload = {"q[activities_activity_type_name_eq]": "hiking",
               "q[city_cont]": city, "q[state_cont]": state, "q[country_cont]": "United+States",
               "radius": radius, "limit": 10}

    # Encoding payload values for adding it to the URL
    # Using urllib to encode params to URL, replace encoded characters to the URL compatible chars
    param_url = urllib.urlencode(payload).replace('%5D', ']').replace('%5B', '[').replace('%2B', '+')

    # Concatenating base_url with final_url, to get the final_url to pass to API request.get
    final_url = base_url + param_url
    my_key = os.environ["X_MASHAPE_KEY"]
    headers = {"X-Mashape-Key": my_key, "Accept": "text/plain"}

    response = requests.get(final_url, headers=headers)
    results = response.json()

    return results


# Helper function for the /loc-results route
# Takes the form inputs, and returns the jsonified data
# Nee
def get_curr_loc(curr_lat, curr_long, radius):
    """Get inputs from the search page, return json data to the calling function"""

    base_url = "https://trailapi-trailapi.p.mashape.com/?"

    # params values for the request object
    payload = {"q[activities_activity_type_name_eq]": "hiking",
               "lat": curr_lat, "lon": curr_long, "limit": 20,
               "radius": radius}

    # Encoding payload values for adding it to the URL
    # Using urllib to encode params to URL, replace encoded characters to the URL compatible chars
    param_url = urllib.urlencode(payload).replace('%5D', ']').replace('%5B', '[').replace('%2B', '+')

    # Concatenating base_url with final_url, to get the final_url to pass to API request.get
    final_url = base_url + param_url
    my_key = os.environ["X_MASHAPE_KEY"]
    headers = {"X-Mashape-Key": my_key, "Accept": "text/plain"}

    response = requests.get(final_url, headers=headers)
    results = response.json()

    return results


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
        d['lat'] = result_list[i]["lat"]
        d['lng'] = result_list[i]["lon"]
        # appending the lat, long value of dictionary to the list of latlong
        latlong_list.append(d)
        # The dictionary is made empty again, to avoid over-writing same
        # dict values, all over the list.
        d = {}
    return latlong_list
    ###################################################################################
    # @Note: REDUNDANT CODE:
    # Need to integrate it with get_address method

    # NOTE: ONLY the 'payload' param varies from the get_address method here
    # Return value is the same as get_address method