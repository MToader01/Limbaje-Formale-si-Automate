import itertools

alphabet = ['a', 'b', 'c', 'd']
language = []

# Generare cuvinte din limbajul formal L
for word_length in range(1, 7):
    for combination in itertools.product(alphabet, repeat=word_length):
        if len(set(combination)) <= 3:  # Verificare dacă există exact 3 litere dublate
            language.append(''.join(combination))

print("Limbajul formal L generat:")
print(language)

# Definirea automatului finit M
Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b', 'c', 'd'}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q0', 'c'): 'q0',
    ('q0', 'd'): 'q0',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q1', 'c'): 'q1',
    ('q1', 'd'): 'q1',
    ('q2', 'a'): 'q2',
    ('q2', 'b'): 'q2',
    ('q2', 'c'): 'q2',
    ('q2', 'd'): 'q2',
    ('q3', 'a'): 'q3',
    ('q3', 'b'): 'q3',
    ('q3', 'c'): 'q3',
    ('q3', 'd'): 'q3'
}
initial_state = 'q0'
final_states = {'q3'}

# Afisarea automatului finit M
print("\nAutomatul finit M=(Q,Σ,δ,q0,F):")
print("Stari: ", Q)
print("Alfabet: ", Sigma)
print("Functia de tranzitie:")
for transition in delta:
    print(f"δ({transition[0]}, {transition[1]}) = {delta[transition]}")
print("Starea initiala: ", initial_state)
print("Stari finale: ", final_states)


import random

# Alegerea aleatoare a 3 cuvinte din limbajul formal L
random_words = random.sample(language, 3)

# Verificarea dacă cuvintele alese sunt în limbajul L
print("\nVerificarea dacă cuvintele alese sunt în limbajul L:")
for word in random_words:
    if word in language:
        print(f"{word} este în limbajul L.")
    else:
        print(f"{word} nu este în limbajul L.")
