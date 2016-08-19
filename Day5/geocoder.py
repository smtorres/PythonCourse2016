from pygeocoder import Geocoder
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
results = Geocoder.geocode(whitehouse)
lat, lng = results[0].coordinates
reverseCode = Geocoder.reverse_geocode(lat, lng)

#https://bitbucket.org/xster/pygeocoder/wiki/Home
