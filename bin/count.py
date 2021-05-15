"""
Prints the total number of sentences and tokens in the corpus files given as
arguments.
"""

import sys


if __name__ == '__main__':
    total_sentences = 0
    total_tokens = 0

    for file_name in sys.argv[1:]:
        with open(file_name) as file:
            for line in file:
                total_sentences += 1
                tokens = line.split()
                total_tokens += len(tokens)

    print(total_sentences, total_tokens)

