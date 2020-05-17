# TB
Consuming World Bank API using Flask to get Capital, Longitude, Latitude from the list of Countries

Step 1:
Get the JSON data from API using Requests.get 

Step 2:
Parse the JSON data

Step 3:
Make a list of all the countries and keep it in "countryName"
Make a Dictionary of all the CapitalCity with Country as key and Capital as Value in "capitalCityDict"
Make a Dictionary of all the Longitude with Country as key and Longitude as Value in "longitudeDict"
Make a Dictionary of all the Latitude with Country as key and Latitude as Value in "latitudeDict"

Step 4:
Make sure we are receiving response from API by using try-except block and appropriate message for any response status other than "OK"

Step 5:
Pass the countryName list created above to "index.html" and render that template
"index.html" has one form containing dropdown(the list of countries) and a submit button which redirects to "result.html" which displays the required data.
 



