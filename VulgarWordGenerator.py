from itertools import product

leet_map = {
    'A': ['A', '4'], 'a': ['a', '4'],
    'E': ['E', '3'], 'e': ['e', '3'],
    'I': ['I', '1'], 'i': ['i', '1'],
    'L': ['L', '1'], 'l': ['l', '1'],
    'O': ['O', '0'], 'o': ['o', '0'],
    'S': ['S', '5'], 's': ['s', '5'],
    'T': ['T', '7'], 't': ['t', '7'],
    'G': ['G', '6', '9'], 'g': ['g', '6', '9'],
    'Z': ['Z', '5'], 'z': ['z', '5'],

    '0': ['0', 'O', 'o'],
    '1': ['1', 'I', 'i', 'L', 'l'],
    '3': ['3', 'E', 'e'],
    '4': ['4', 'A', 'a'],
    '5': ['5', 'S', 's', 'Z', 'z'],
    '6': ['6', 'G', 'g'],
    '7': ['7', 'T', 't'],
    '9': ['9', 'G', 'g'],
}

input_text = input("Enter text to generate leetspeak combinations\n(put ^ at the end to include lowercase replacing): ")

include_lowercase = input_text.endswith('^')
if include_lowercase:
    input_text = input_text[:-1]

options = []
for char in input_text:
    if char in leet_map:
        variants = leet_map[char]
        if not include_lowercase:
            variants = [v for v in variants if not v.islower()]
        options.append(variants)
    else:
        options.append([char])

combinations = [''.join(variant) for variant in product(*options)]

print(f"\nGenerated {len(combinations)} combinations:\n")
for combo in combinations:
    print(combo)