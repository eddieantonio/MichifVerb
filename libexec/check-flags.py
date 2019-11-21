#!/usr/bin/env python3

import re
import sys

flag_pattern = re.compile(r'@\w[.]\w+(?:[.]\w+)@')

defined_flags = set()
undefined_flags = set()


def collect_vocab(flag, lineno):
    if flag in defined_flags:
        print(f"{lineno}:warning: already defined: {flag}")
    defined_flags.add(flag)


def check_if_defined(flag, lineno):
    if flag in defined_flags:
        return
    print(f"{lineno}:error: found undefined flag: {flag}")
    undefined_flags.add(flag)


on_flag = collect_vocab

for lineno, line in enumerate(sys.stdin, start=1):
    if line.lstrip().startswith('LEXICON'):
        on_flag = check_if_defined

    matches = flag_pattern.findall(line)
    for flag in matches:
        on_flag(flag, lineno)

if undefined_flags:
    sys.exit(1)