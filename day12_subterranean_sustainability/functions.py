"""
Functions for Advent of Code 2018, Day 12: Subterranean Sustainability
"""

import copy
from collections import deque
import regex as re

def count(items, zeroth, target):
    count = 0
    indices = [num for num in range(0 - zeroth, len(items) - zeroth)]
    for num in range(len(items)):
        if items[num] == target:
            count += indices[num]
    return count


def extend_string(string, zeroth, target, adjunct):
    for i in range(2):
        position = 0
        for item in string:
            if item == target:
                while len(string[:position]) < 5:
                    string = adjunct + string
                    if i is 0:
                        zeroth += 1
                    position += 1
                break
            position += 1
        string = string[::-1]
        i += 1
    return string, zeroth


def define_region(string, position):
    return string[position - 2 : position + 3]


def reduce_string(string, zeroth, target, adjunct):
    for i in range(2):
        while string.startswith("o" * 10):
            string = string[5:]
            if i is 0:
                zeroth -= 5
        string = string[::-1]
        i += 1
    return string, zeroth


def update(string, rules):
    new_string = "o" * len(string)
    for rule in rules:
        p = re.compile(rule)
        for match in p.finditer(string, overlapped = True):
            match_start, match_end = match.span()
            new_string = new_string[:match_start + 2] + "#" + new_string[match_start + 3:]
    return new_string