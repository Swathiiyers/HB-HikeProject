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


    <script>

      function getSearches(evt){

        evt.preventDefault();
        // if (past_searches.length > 0){
        //   console.log("i successfully checked length");
        //   var past_searches = {{ past_searches | tojson }};
          $('.search-info').text("success");


        console.log("success");
      }

      // function displaySearches(past_searches){
      //   console.log("i come here");
      //   for (let search in past_searches){

      //     $('.search-info').append(search.city);
      //   }

        
            // var btn = document.createElement("BUTTON");
            // var t = document.createTextNode("CLICK ME");
            // btn.appendChild(t);
            // $('.search-info').append(btn);

      $('#user-search').click(getSearches);



    </script>


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


# User profile code:
# {% extends 'base.html' %}
# {% block title %}User Profile{% endblock %}
    
#     {% block content %}
    
#     <p>Welcome, {{ session["user_name"] }}</p>

#     <nav class="navbar navbar-default sidebar" role="navigation">
#         <div class="container-fluid">
#         <div class="navbar-header">
#           <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-sidebar-navbar-collapse-1">
#             <span class="sr-only">Toggle navigation</span>
#             <span class="icon-bar"></span>
#             <span class="icon-bar"></span>
#             <span class="icon-bar"></span>
#           </button>
#         </div>
#         <div class="collapse navbar-collapse" id="bs-sidebar-navbar-collapse-1">
#           <ul class="nav navbar-nav">
#             <li class="active"><a href="#">Home<span style="font-size:16px;" class="pull-right hidden-xs showopacity glyphicon glyphicon-home"></span></a></li>
#                 <li><a href="#">Past searches</a></li>
#                 <li><a href="#">Ratings</a></li>
#                 <li class="divider"></li>
#               </ul>
#             </li>
#           </ul>
#         </div>
#       </div>
#     </nav>

#     </div>

new_comment = Comment(user_id=1, trail_id=293, comment_description="Enjoyed the hike. Spectacular views! Recommend to all nature lovers")
new_comment2 = Comment(user_id=1, trail_id=280, comment_description="Awesome hike! Lovely time with friends and family")

new_rating = Rating(user_id=1, trail_id=293, score=4)
new_rating2 = Rating(user_id=1, trail_id=280)

new_review = Review(user_id=1, trail_id=293, score=4, comment_description="Awesome hike! Lovely time with friends and family")
new_review2 = Review(user_id=1, trail_id=280, comment_description="Enjoyed the hike. Spectacular views! Recommend to all nature lovers" )




         <div class="navbar-header">
           <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="bs-sidebar-navbar-collapse-1">
             <span class="sr-only">Toggle navigation</span>
             <span class="icon-bar"></span>
             <span class="icon-bar"></span>
             <span class="icon-bar"></span>
           </button>      
         </div>





