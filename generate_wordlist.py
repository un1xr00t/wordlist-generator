# generate_wordlist.py

import itertools

def generate_wordlist(characters, min_length, max_length):
    wordlist = []
    for length in range(min_length, max_length + 1):
        for word in itertools.product(characters, repeat=length):
            wordlist.append(''.join(word))
    return wordlist

# Example usage
characters = 'abc123'
min_length = 1
max_length = 3
wordlist = generate_wordlist(characters, min_length, max_length)

# Save to file
with open('generated_wordlist.txt', 'w') as f:
    for word in wordlist:
        f.write(f"{word}\n")
