#!/usr/bin/env python3

"""
Script that makes sure all flag diacritics used in the lexicon have been
properly defined.

NOTE: uses tonnes of globals. Be aware before refactoring!
"""

import re
import sys
import fileinput

# What does a flag look like?
flag_pattern = re.compile(r'@\w[.]\w+(?:[.]\w+)@')


defined_flags = set()
undefined_flags = set()


def collect_vocab(flag):
    if flag in defined_flags:
        emit(f"already defined: {bold(flag)}", level="warning")
    defined_flags.add(flag)


def check_if_defined(flag):
    if flag in defined_flags:
        return
    emit(f"found undefined flag: {bold(flag)}")
    undefined_flags.add(flag)


def emit(message, level='error'):
    lineno = fileinput.filelineno()
    filename = fileinput.filename()
    print(f"{filename}:{lineno}: {red(level)}: {message}", file=sys.stderr)

def green(s):
    return f"\033[32m{s}\033[m"


def red(s):
    return f"\033[31m{s}\033[m"


def bold(s):
    return f"\033[1m{s}\033[m"


on_flag = collect_vocab

for line in fileinput.input():
    if line.lstrip().startswith('LEXICON'):
        on_flag = check_if_defined

    matches = flag_pattern.findall(line)
    for flag in matches:
        on_flag(flag)

# Exit with error if there are undefined flags:
if undefined_flags:
    sys.exit(1)
else:
    print(green("Flag diacritics look ok!"), file=sys.stderr)
