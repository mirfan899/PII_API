import re
# (A|B[1-7]?|M|T|C[1-4]|D)
# medical_id = re.compile("^[0-9]{3}(-)?[0-9]{2}(-)?[0-9]{4}$")
# medical_id = re.compile(r"[0-9]{3}(-)[0-9]{2}(-)[0-9]{4}")
medical_id = r"\b\d{3}(-)\d{2}(-)\d{4}(A|B[1-7]?|M|T|C[1-4]|D)\b"
license_plates_usa = re.compile(r"[A-Z]{1,3}(-)?([A-Z]{1,2})?(-)?[0-9]{1,4}")
# license_plates_usa = r"\b[A-Z]{1,3}(-)?([A-Z]{1,2})?(-)?[0-9]{1,4}"


print(re.match(license_plates_usa, "this is a plate CCX-4344"))
matches = re.finditer(license_plates_usa, "this is a plate CCX-4344")

for matchNum, match in enumerate(matches, start=1):
    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

# print(license_plates_usa.match("TU-250"))
# print(license_plates_usa.match("EK3333"))
# print(license_plates_usa.match("7AAXS8"))
# print(license_plates_usa.match("532884"))

matches = re.finditer(medical_id, "this is a medical id 315-77-8771, A 002-51-3788B2")

for matchNum, match in enumerate(matches, start=1):
    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))
