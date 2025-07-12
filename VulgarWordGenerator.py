from itertools import product

leet_map = {
    'A': ['A', '4'], 'a': ['a', '4'],
    'E': ['E', '3'], 'e': ['e', '3'],
    'I': ['I', '1'], 'i': ['i', '1'],
    'L': ['L', '1'], 'l': ['l', '1'],
    'O': ['O', '0'], 'o': ['o', '0'],
    'S': ['S', '5'], 's': ['s', '5'],
    'T': ['T', '7'], 't': ['t', '7'],
    'G': ['G', '6'], 'g': ['g', '6']
}

input_text = input("Enter text to generate leetspeak combinations: ")

options = []
for char in input_text:
    if char in leet_map:
        options.append(leet_map[char])
    else:
        options.append([char])

combinations = [''.join(variant) for variant in product(*options)]

print(f"\nGenerated {len(combinations)} combinations:\n")
for combo in combinations:
    print(combo)