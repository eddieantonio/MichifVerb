#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Pretty prints ALL pairs from Foma
"""

import io
import subprocess
import sys
import tempfile
from collections import defaultdict


MAX_WORDS = 10_000


fomabin = sys.argv[1]

words: bytes = subprocess.check_output(['foma', '-q', '-e', f'load stack {fomabin}', '-e', f'print upper-words {MAX_WORDS}', '-s'])
with tempfile.TemporaryFile('w+b') as input_file:
    input_file.write(words)
    input_file.flush()
    # Go back to the start, so that Foma can start reading from the beginning:
    input_file.seek(0)
    lookups: bytes = subprocess.check_output(['flookup', '-i', fomabin], stdin=input_file)

# Let's organize the output:
analysis2wordforms = defaultdict(set)
for line in lookups.decode('UTF-8').split('\n'):
    if not line.strip():
        continue

    analysis, _tab, wordform = line.partition('\t')
    analysis2wordforms[analysis].add(wordform)

# Figure out how wide the first column should be:
max_analysis_len = len(max(analysis2wordforms.keys(), key=len))

# Now print all nice and pretty, sorted by lemma:
for analysis in sorted(analysis2wordforms.keys()):
    wordforms = analysis2wordforms[analysis]
    for wordform in sorted(wordforms, key=len):
        print(f"{{0:<{max_analysis_len}s}}\t{{1}}".format(analysis, wordform))
