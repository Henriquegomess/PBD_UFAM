#!/usr/bin/env python

import sys
import io
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

word_count = {}

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
for line in input_stream:
    line = line.strip().lower()

    words = re.findall(r'[A-Za-z]+', line)
    for word in words:
        if word not in stop_words:
            word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print('%s\t%s' % (word, count))

