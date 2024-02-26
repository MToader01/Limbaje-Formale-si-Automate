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


grammar_a = {
    'V': {'S', 'A', 'B'},
    'T': {'a', 'b'},
    'S': 'AB',
    'P': {
        'S': ['AB'],
        'A': ['aA', ''],
        'B': ['bB', '']
    }
}


generated_strings_a = generate_strings(grammar_a)
print("a) Șirurile generate:")
print(generated_strings_a)
