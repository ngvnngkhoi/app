import phonenumbers
#from main import test_number
from phonenumbers import geocoder

pepnumber = phonenumbers.parse('+61455512511')
location =  geocoder.description_for_number(pepnumber,'en')
print(location)