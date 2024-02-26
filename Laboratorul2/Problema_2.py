def generate_strings(iterations):
    strings = ['a', 'b']  

   
    def apply_rules(string):
        if len(string) >= iterations:  
            return [string]
        else:
            new_strings = []
            
            for char in ['a', 'b']:
                new_string = char + string + char
                new_strings.extend(apply_rules(new_string))
            return new_strings


    for _ in range(iterations - 1):
        new_strings = []
        for string in strings:
            new_strings.extend(apply_rules(string))
        strings = new_strings

    return strings

#
iterations = 3


for i in range(1, iterations + 1):
    generated_strings = generate_strings(i)
    print(f"Iterația {i}: {', '.join(generated_strings)}")
