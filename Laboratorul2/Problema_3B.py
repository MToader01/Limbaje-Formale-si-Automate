def generate_strings(grammar):
    strings = ['S'] 

  
    def apply_rules(string):
        new_strings = [string] 

        for i, char in enumerate(string):
            if char in grammar['V']:
                for rule in grammar['P'][char]:
                    new_string = string[:i] + rule + string[i+1:]  
                    new_strings.extend(apply_rules(new_string)) 

        return new_strings

  
    while any(char in grammar['V'] for char in strings[0]):
        new_strings = []
        for string in strings:
            new_strings.extend(apply_rules(string))
        strings = new_strings

    return strings


grammar_b = {
    'V': {'S', 'X', 'Y', 'Z'},
    'T': {'0', '1', '2', '3', '4'},
    'S': 'X',
    'P': {
        'X': ['0Y', '1Z'],
        'Y': ['2', 'X'],
        'Z': ['3', '4', 'X']
    }
}


generated_strings_b = generate_strings(grammar_b)
print("\nb) Șirurile generate:")
print(generated_strings_b)
