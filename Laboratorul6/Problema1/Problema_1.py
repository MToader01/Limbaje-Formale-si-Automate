import re

# Definim expresia regulată
regex = r'(1+00*1)|(1+00*1)(0+10*1)*(0+10*1)'
pattern = re.compile(regex)

# Testăm câteva cazuri
test_cases = ["001", "101", "1001", "1101", "10001", "10001101", "100011001"]
for test in test_cases:
    if pattern.fullmatch(test):
        print(f"Match found for {test}")
    else:
        print(f"No match found for {test}")
