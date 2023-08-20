#  Nominatim is a free service or tool or can be called an API with no keys that provide you with the data after providing it with name and address and vice versa.

# importing geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# entering the location name
getLoc = loc.geocode(" Dharavi, Mumbai, Maharashtra 400016")

# printing address
print(getLoc)
print(getLoc.address)

# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)
