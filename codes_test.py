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

nav.sidebar, .main{
    -webkit-transition: margin 200ms ease-out;
      -moz-transition: margin 200ms ease-out;
      -o-transition: margin 200ms ease-out;
      transition: margin 200ms ease-out;
  }

  .main{
    padding: 10px 10px 0 10px;
  }

 @media (min-width: 765px) {

    .main{
      position: absolute;
      width: calc(100% - 40px); 
      margin-left: 40px;
      float: right;
    }

    nav.sidebar:hover + .main{
      margin-left: 200px;
    }

    nav.sidebar.navbar.sidebar>.container .navbar-brand, .navbar>.container-fluid .navbar-brand {
      margin-left: 0px;
    }

    nav.sidebar .navbar-brand, nav.sidebar .navbar-header{
      text-align: center;
      width: 100%;
      margin-left: 0px;
    }
    
    nav.sidebar a{
      padding-right: 13px;
    }

    nav.sidebar .navbar-nav > li:first-child{
      border-top: 1px #e5e5e5 solid;
    }

    nav.sidebar .navbar-nav > li{
      border-bottom: 1px #e5e5e5 solid;
    }

    nav.sidebar .navbar-nav .open .dropdown-menu {
      position: static;
      float: none;
      width: auto;
      margin-top: 0;
      background-color: transparent;
      border: 0;
      -webkit-box-shadow: none;
      box-shadow: none;
    }

    nav.sidebar .navbar-collapse, nav.sidebar .container-fluid{
      padding: 0 0px 0 0px;
    }

    .navbar-inverse .navbar-nav .open .dropdown-menu>li>a {
      color: #777;
    }

    nav.sidebar{
      width: 200px;
      height: 100%;
      margin-left: -160px;
      float: left;
      margin-bottom: 0px;
    }


    nav.sidebar li {
      width: 100%;
    }

    nav.sidebar:hover{
      margin-left: 0px;
    }

    .forAnimate{
      opacity: 0;
    }
  }
   
  @media (min-width: 1330px) {

    .main{
      width: calc(100% - 200px);
      margin-left: 200px;
    }

    nav.sidebar{
      margin-left: 0px;
      float: left;
    }

    nav.sidebar .forAnimate{
      opacity: 1;
    }
  }

  nav.sidebar .navbar-nav .open .dropdown-menu>li>a:hover, nav.sidebar .navbar-nav .open .dropdown-menu>li>a:focus {
    color: #CCC;
    background-color: transparent;
  }

  
  nav:hover .forAnimate{
    opacity: 1;
  }
  section{
    padding-left: 15px;
  }

.fa {
  padding: 20px;
  font-size: 30px;
  width: 30px;
  text-align: center;
  text-decoration: none;
  margin: 5px 2px;
  float: right;
  position: relative;
  display: inline;
}
.fa-facebook {
  background: #3B5998;
  color: white;
}

.fa-twitter {
  background: #55ACEE;
  color: white;
}

.checked {
    color: orange;
}

.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button:hover, a:hover {
  opacity: 0.7;
}


.bg_blur
{
    background-image:url('http://data2.whicdn.com/images/139218968/large.jpg');
    height: 300px;
    background-size: cover;
}

