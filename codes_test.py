# Below is the Code to customize URL for making API calls to TrailAPI (city-based search)

import requests
import urllib

base_url = "https://trailapi-trailapi.p.mashape.com/?"

# params values for the request object
payload = {"q[activities_activity_type_name_eq]": "hiking", "q[city_cont]": "san+jose", "q[state_cont]": "California", "radius": 20}

# Encoding payload values for adding it to the URL
# Using urllib to encode params to URL, replace encoded characters to the URL compatible chars
param_url = urllib.urlencode(payload).replace('%5D', ']').replace('%5B', '[').replace('%2B', '+')

# Concatenating base_url with final_url, to get the final_url to pass to API request.get
final_url = base_url + param_url
headers = {"X-Mashape-Key": "rQoJ3qTszpmshKM5FExXPQ4NDLQlp1lvWp9jsnwPbf3Lwcutq7", "Accept": "text/plain"}

response = requests.get(final_url, headers=headers)
results = response.json()

result_list = results["places"]

# Initializing list of Latlong values
latlong_list = []

# Dictionary of latlong value, for each latlong pair (from search results)
d = {}

# For loop to append each latlong pair to the list of latlong dict (d)

for i in range(len(result_list)):
    print result_list[i]["name"]
    print result_list[i]["unique_id"]
    print result_list[i]["activities"][0]["description"]
    print result_list[i]["activities"][0]["url"]
    print result_list[i]["activities"][0]["length"]
    print "\n"
    # print "\n"

# code for checking length
    # <script>

    #   function getSearches(evt){

    #     evt.preventDefault();
    #     // if (past_searches.length > 0){
    #     //   console.log("i successfully checked length");
    #     //   var past_searches = {{ past_searches | tojson }};
    #       $('.search-info').text("success");


    #     console.log("success");
    #   }

    #   // function displaySearches(past_searches){
    #   //   console.log("i come here");
    #   //   for (let search in past_searches){

    #   //     $('.search-info').append(search.city);
    #   //   }

    #         // var btn = document.createElement("BUTTON");
    #         // var t = document.createTextNode("CLICK ME");
    #         // btn.appendChild(t);
    #         // $('.search-info').append(btn);

    #   $('#user-search').click(getSearches);



    # </script>


    # appending the lat, long value of dictionary to the list of latlong




#Access the URL, rating, description

# >>> results["places"][0]["lat"][0]["url"]
# u'http://www.tripleblaze.com/trail.php?c=3&i=258'

# >>> results["places"][0]["activities"][0]["rating"]
# 0.0

# >>> results["places"][0]["activities"][0]["description"]
# u'Alum Rock Park features 5 miles of hiking trails near San Jose, CA.'

#Notice '1' index , for accessing Description, URL et
# >>> results["places"][1]["activities"][0]["description"]
# u'Joseph D. Grant County Park features 6 miles of hiking trails near San Jose, CA.'
# >>> results["places"][1]["activities"][0]["url"]
# u'http://www.tripleblaze.com/trail.php?c=3&i=1060'
# >>> results["places"][1]["activities"][0]["name"]
# u'Joseph D. Grant County Park'


# Code for finding lat, long of the search place:
# >>> results["places"][0]["lat"]
# 37.39354
# >>> results["places"][0]["lon"]
# -121.81572



# Jinja display of other fields:

#  <!--            <li>Hiking Trail ID: {{ (result["unique_id"]) }}</li>
#             <li>Description: {{ (result["description"]) }}</li>
#             <li>Directions: {{ (result["directions"]) }}</li>
#             <li>Latitude: {{ (result["lat"]) }}</li>
# #             <li>Longitude: {{ (result["lon"]) }}</li><br><br> -->
# Take inputs from position.coords.lat and pass them into hidden inputs, from hidden inputs, pass values to python server
# navigator.geolocation.getCurrentPosition( function (position) { alert(position.coords.latitude) })

# button.addEventListener('click', function () {

# navigator.geolocation.getCurrentPosition( function(position) {

# new_comment = Comment(user_id=1, trail_id=293, comment_description="Enjoyed the hike. Spectacular views! Recommend to all nature lovers")
# new_comment2 = Comment(user_id=1, trail_id=280, comment_description="Awesome hike! Lovely time with friends and family")

# new_rating = Rating(user_id=1, trail_id=293, score=4)
# new_rating2 = Rating(user_id=1, trail_id=280)

# new_review = Review(user_id=1, trail_id=293, score=4, comment_description="Awesome hike! Lovely time with friends and family")
# new_review2 = Review(user_id=1, trail_id=280, comment_description="Enjoyed the hike. Spectacular views! Recommend to all nature lovers" )
# new_review3 = Review(user_id=2, trail_id=293, score=5, comment_description="Must-do place in every hiker's list! Great place to enjoy a sunny weekend morning!" )

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Individual result page</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>


{% extends 'base.html' %}
{% block title %}Results Page{% endblock %}

   {% block content %}

    {% if "user_name" in session %}
    <h2> Hey, {{ session["user_name"] }}</h2>
    {% endif %}




