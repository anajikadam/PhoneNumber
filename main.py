import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier

print("Hello")
print("Phone Number : ", number)

ch_number = phonenumbers.parse(number, "CH") # C Contry H History
country = geocoder.description_for_number(ch_number, "en")
print("Country For the Number is ", country)

service_number = phonenumbers.parse(number, "RO") #Ro region
carrier = carrier.name_for_number(service_number, "en")
print("Carrier for the number is ", carrier)

print("End...")

