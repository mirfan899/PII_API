### PII(Personal Identifiable Information)
I'm using `presidio` and `spacy` to identify PII from text. Currently following information is being detected

```text
CREDIT_CARD
CRYPTO
DATE_TIME
EMAIL_ADDRESS
IBAN_CODE
IP_ADDRESS
NRP
LOCATION
PERSON
PHONE_NUMBER
MEDICAL_LICENSE
URL
```

Following entities will be added.
```text
Bank account numbers
Investment account numbers
Street addresses
Date of birth
State ID card numbers
Maiden names
Health care number/member IDs
License plate numbers
Vehicle identification numbers (VIN)
Social media accounts
MAC addresses
Cryptocurrency addresses, yes(bitcoin)
Medical records
Health care/insurance
Student records
HR records
Legal numbers
General accounts numbers
Policy numbers
Insurance Policy numbers
```

### Helpful links

```text
https://regexlib.com/UserPatterns.aspx?authorid=294cee08-6163-49c8-9534-922f149a2a16
```