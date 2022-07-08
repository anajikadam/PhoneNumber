import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
x = "+917499094274"
ch_number = phonenumbers.parse(x, "CH")
a = geocoder.description_for_number(ch_number, "hi")
print(a)

gb_number = phonenumbers.parse(x, "GB")
tz = timezone.time_zones_for_number(gb_number)
print(tz)

