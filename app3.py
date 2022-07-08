import phonenumbers
# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
phoneNumber = phonenumbers.parse("+919876543210")

# This will print the phone number and
# it's basic details.
print(phoneNumber)
text = "Contact us at +919876543210 or +14691234567"

# Pass the text and country code to the below function
numbers = phonenumbers.PhoneNumberMatcher(text, "IN")

# Printing the phone numbers matched with country code
# and also the indexes of the phone numbers in the string input
for number in numbers:
    print(number)

# Parsing String to Phone number
phone_number = phonenumbers.parse("+91987654321")
phone_number = phonenumbers.parse("+917499097276")

# Validating a phone number
valid = phonenumbers.is_valid_number(phone_number)

# Checking possibility of a number
possible = phonenumbers.is_possible_number(phone_number)

# Printing the output
print(valid)
print(possible)

