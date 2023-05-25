Text = input("Vaša veta: ")

vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,
    'A': 0,
    'E': 0,
    'I': 0,
    'O': 0,
    'U': 0,

}

for c in Text:
    c = c.lower()
    if c in vowels:
        vowels[c] += 1

for v in vowels:
    if vowels[v] > 0:
        print(v, ":", vowels[v])