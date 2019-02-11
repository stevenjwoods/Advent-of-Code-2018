# Steven Woods
# Advent of Code 2018
# Day 12: Subterranean Sustainability
# To run: python3 sustain.py <path/to/input.txt>

import sys

import regex as re

import functions

with open(sys.argv[1], "r") as f:
    text = f.readlines()
    text = [line.strip() for line in text]

iterations = int(input("Enter the number of iterations: "))

rules = []
zeroth = 0
for line in text:
    line = re.sub("\.", "o", line)
    if "initial" in line:
        *head, state = line.split()
    elif "=> #" in line:
        sub_state, _, result = line.split()
        rules.append(sub_state)

#print(f"i.0:\t{state}")
for i in range(iterations):
    state, zeroth = functions.extend_string(state, zeroth, "#", "o")
    state, zeroth = functions.reduce_string(state, zeroth, "#", "o")
    state = functions.update(state, rules)
#    print(f"i.{i + 1}:\t{state}")

count = functions.count(state, zeroth, "#")
print(f"After {iterations} iterations, the sum of the values of pots containing plants is {count}.")