def concat(s1, s2):
    return s1 + s2

def repeat(s, n):
    return s * n

def reverse(s):
    return s[::-1]

def extract(s, i, j):
    return s[i-1:j]

def replace(s, sub, new_sub):
    return s.replace(sub, new_sub, 1)

def apply_operations(word):
    # Definim alfabetele
    alphabet1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k']
    alphabet3 = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5']

    
    result = {
        "Concatenare cu alfabetul 2": concat(word, ''.join(alphabet2)),
        "Repetare de 3 ori": repeat(word, 3),
        "Inversare": reverse(word),
        "Extracție de la poziția 2 la 5": extract(word, 2, 5),
        "Înlocuirea primei apariții a 'a' cu 'x1'": replace(word, 'a', 'x1')
    }

    return result


word = "ABC"
result = apply_operations(word)
for operation, value in result.items():
    print(operation + ":", value)
