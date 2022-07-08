import phonenumbers
text = "Call me at 7499094276 if it's before 9:30, or on 703-4800500 after 10am."
for match in phonenumbers.PhoneNumberMatcher(text, "IN"):
    print(match)
for match in phonenumbers.PhoneNumberMatcher(text, "IN"):
    print(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))