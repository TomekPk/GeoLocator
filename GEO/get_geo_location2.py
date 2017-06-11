# remember to pip install geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()
my_address = input("Enter new address to check: ")
location = geolocator.geocode(my_address, timeout=2)
print(location.address)
print(location.latitude, location.longitude)
print("\n")
