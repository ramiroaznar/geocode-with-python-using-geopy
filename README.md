# Geocode your csv files with Python using Geopy

A Python program to geocode a csv file using Geopy. This was used to geocode addresses from a list of Spanish bank offices.

## geocode-with-geopy.py

Script to geocode a csv file, adding two new columns with longitude and latitude values.

## csv-files

Four csv files containing the bank, address, city and country of four Spanish bank offices of the city of Madrid: *banco_popular.csv*, *bankinter.csv*, *cajamar.csv* and *caja_laboral.csv*. Source: http://www.cajerosybancos.es/

## csv-geo-files

Four geocoded csv files containing the bank, address, longitude, latitude, city and country of four Spanish bank offices of the city of Madrid: *banco_popular_geo.csv*, *bankinter_geo.csv*, *cajamar_geo.csv* and *caja_laboral_geo.csv*.

## Final thoughts

First, because Geopy has a limit of 500 items, it would be necessary to write a "if adress is already in the new file" statement in order to avoid repetition and conserve the geocoding budget. Secondly, the resulting *_geo.csv* files were in a bad format (separated by lines). In order to solve this, I will try not to use the csv module. Third, it would be better to save the new data in a database such as SQLITE or Postgres. Finally, lots of data points were wrongly geocoded. In order to debug this, two things can be tried. One is using the address with the city and country together, and the other is using a if statement with a buffer postgis funcion to remove all the data points not situated in Madrid city.

