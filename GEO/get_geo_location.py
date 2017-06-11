# remember to pip install geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()
my_address="Bielsk Podlaski"
location = geolocator.geocode(my_address, timeout=2)
print(location.address)
print(location.latitude, location.longitude)
