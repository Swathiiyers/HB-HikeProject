// let searchButton = document.querySelector('#search-button');

function showAlertMessage(evt) {
// prevent buttonClick from navigating to the route.

    "use strict";
    evt.preventDefault();
    console.log("I come here");
    alert('Submitted successfully');
}

// searchButton.addEventListener("click", showAlertMessage);


var searchButton = document.getElementById("search-form");

searchButton.addEventListener("click",showAlertMessage);

