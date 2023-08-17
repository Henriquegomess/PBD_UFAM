#!/usr/bin/env python

import sys

current_word = None
current_count = 0

for line in sys.stdin:
    word, count = line.strip().split('\t', 1)

    if current_word != word:
        if current_word is not None:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = 0

    current_count += int(count)

if current_word is not None:
    print(f"{current_word}\t{current_count}")

