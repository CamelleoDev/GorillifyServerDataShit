from itertools import product

leet_map = {
    'A': ['A', '4'],
    'E': ['E', '3'],
    'I': ['I', '1'],
    'L': ['L', '1'],
    'O': ['O', '0'],
    'S': ['S', '5'],
    'T': ['T', '7'],
    'G': ['G', '6']
}

input_text = input("Enter text to generate leetspeak combinations: ").upper()

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