def generate_strings(iterations):
    strings = ['a', 'b']  # Inițializăm lista de șiruri cu cele două șiruri de lungime 1

    # Funcția pentru aplicarea regulilor de producție
    def apply_rules(string):
        if len(string) >= iterations:  # Nu mai aplicăm regulile dacă șirul a atins lungimea dorită
            return [string]
        else:
            new_strings = []
            # Regulile de producție
            for char in ['a', 'b']:
                new_string = char + string + char
                new_strings.extend(apply_rules(new_string))
            return new_strings

    # Aplicăm regulile de producție de 'iterations' ori
    for _ in range(iterations - 1):
        new_strings = []
        for string in strings:
            new_strings.extend(apply_rules(string))
        strings = new_strings

    return strings

# Numărul de iterații
iterations = 3

# Generăm și afișăm șirurile pentru cele trei iterații
for i in range(1, iterations + 1):
    generated_strings = generate_strings(i)
    print(f"Iterația {i}: {', '.join(generated_strings)}")
