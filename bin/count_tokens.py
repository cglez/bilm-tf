"""
Counts the number of tokens in the corpus files given as arguments.
"""

import sys

if __name__ == '__main__':
    total = 0

    for file_name in sys.argv[1:]:
        with open(file_name) as file:
            for line in file:
                tokens = line.split()
                total += len(tokens)

    print(total)
