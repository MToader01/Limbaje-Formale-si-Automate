import re

def test_regex(regex, test_cases):
    pattern = re.compile(regex)
    for test in test_cases:
        if pattern.fullmatch(test):
            print(f"'{test}' matches the regular expression.")
        else:
            print(f"'{test}' does not match the regular expression.")

# Test 1
regex_1 = r'0+1+'
test_cases_1 = ['0', '00', '001', '0001', '00001', '1', '11', '111', '1111']
print("Test 1:")
test_regex(regex_1, test_cases_1)

# Test 2
regex_2 = r'a+b+'
test_cases_2 = ['a', 'ab', 'abb', 'aabb', 'aabbb', 'b', 'bb', 'bbb', 'bbbb']
print("\nTest 2:")
test_regex(regex_2, test_cases_2)

# Test 3
regex_3 = r'a+b+c+'
test_cases_3 = ['abc', 'aabbcc', 'aaabbbccc', 'ab', 'aabc', 'aabbc', 'aaabbbcccc']
print("\nTest 3:")
test_regex(regex_3, test_cases_3)
