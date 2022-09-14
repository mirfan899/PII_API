import re

medical_id = re.compile("^((\d){3})(-)?(\d){2}(-)?(\d){4}(A|B[1-7]?|M|T|C[1-4]|D)$")

license_plates_usa = re.compile("^[A-Z]{1,3}(-)?([A-Z]{1,2})?(-)?[0-9]{1,4}$")

print(license_plates_usa.match("CCX-4344"))
print(license_plates_usa.match("TU-250"))
print(license_plates_usa.match("EK3333"))
print(license_plates_usa.match("7AAXS8"))
print(license_plates_usa.match("532884"))
