import re

def validate_postal_code(postal_code):
    pattern = re.compile(r'^[1-9][0-9](?=\d{3})\d{3}$')
    if pattern.match(postal_code):
        print(f"The postal code '{postal_code}' is valid.")
    else:
        print(f"The postal code '{postal_code}' is not valid.")

# Testăm câteva coduri poștale
postal_codes = ['12345', '54321', '98765', '10123', '99999', '1234', '123456', 'abcde']
for code in postal_codes:
    validate_postal_code(code)
