def concatenate(s1, s2):
    return s1 + s2

def invers(s):
    return s[::-1]

def substituie(s, a, b):
    return s.replace(a, b)

def lungime(s):
    return len(s)

A = {'a', 'b', 'c'}
B = {'x', 'y', 'z'}
C = {'1', '2', '3'}

s1 = 'abc'
s2 = 'xyz'
s3 = '123'

print("Concatenarea lui s1 și s2:", concatenate(s1, s2))
print("Inversul lui s1:", invers(s1))
print("Substituirea lui 'a' cu '1' în s1:", substituie(s1, 'a', '1'))
print("Lungimea lui s1:", lungime(s1))
