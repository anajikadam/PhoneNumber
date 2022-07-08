import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

xx = "+917499094276"
x = phonenumbers.parse(xx, None)
print(type(x))
y = phonenumbers.parse(xx, "GB")
print(x==y)
a = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
b = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
print(a)
print(b)
