# combine_wordlists.py

import os

def combine_wordlists(output_file, *input_files):
    with open(output_file, 'w') as outfile:
        for fname in input_files:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
            outfile.write("\n")

# Combine all wordlists into one file
generated_wordlist = 'generated_wordlist.txt'
downloaded_wordlists = [os.path.join('wordlists', file) for file in os.listdir('wordlists') if file.endswith('.txt')]

combine_wordlists('combined_wordlist.txt', generated_wordlist, *downloaded_wordlists)
