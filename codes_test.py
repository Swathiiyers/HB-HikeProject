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
    # print result_list[i]["lat"]
    # print result_list[i]["lon"]
    # print "\n"
    d['lat'] = result_list[i]["lat"]
    d['lng'] = result_list[i]["lon"]
    latlong_list.append(d)
    d = {}
    # appending the lat, long value of dictionary to the list of latlong

print latlong_list


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



#     <script tage for findmyloc

# // var x = document.getElementById("demo");

# // function getLocation() {
# //     if (navigator.geolocation) {
# //         navigator.geolocation.getCurrentPosition(showPosition);
# //     } else {
# //         x.innerHTML = "Geolocation is not supported by this browser.";
# //     }
# // }

# // function showPosition(position) {
# //     x.innerHTML = "Latitude: " + position.coords.latitude +
# //     "<br>Longitude: " + position.coords.longitude;
# }



 # document.getElementById("#curr-lat").value =  + position.coords.latitude +
 #  document.getElementById("#curr-long").value = + position.coords.longitude +


 # #######################################################################
# login_form (previous)
#  <!-- {% extends 'base.html' %}
# {% block content %}

#     <h1>Login</h1>
#     <form action="/choose-login" method="POST">
#         <div>
#                 Enter your name:        <input type="text" name="user_name"><br>
#                 Enter your login email: <input type="email" name="email" required><br>
#                 Enter the password:     <input type="password" name="password" required><br>
#                 <input type="submit" value="Log In">
#         </div>

#     </form>
# {% endblock %}


#  -->
