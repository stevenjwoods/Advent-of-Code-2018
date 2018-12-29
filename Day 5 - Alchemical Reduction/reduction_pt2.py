# Steven Woods
# Advent of Code 2018
# Day 5: Alchemical Reduction part 2
# To run: python3 reduction_pt2.py <path/to/input_file>

import sys
inFile = sys.argv[1]
with open(inFile) as f:
	original_polymer = f.read()
original_polymer.strip()

(problematic_unit, smallest_reacted_polymer) = ((), ())
from string import ascii_lowercase
for c in ascii_lowercase:
	polymer = original_polymer.replace(c, "")
	polymer = polymer.replace(c.upper(), "")

	destroyed = ['0']
	i = 0
	while destroyed:
		destroyed = []
		while i < len(polymer) - 1:
			if polymer[i].lower() == polymer[i+1].lower():
				if (polymer[i].isupper() and polymer[i+1].islower()) or (polymer[i].islower() and polymer[i+1].isupper()):
					destroyed = [polymer[i], polymer[i+1]]
					polymer = polymer.replace("{0}{1}".format(polymer[i], polymer[i+1]), "")
			i += 1
		i = 0

	if smallest_reacted_polymer:
		if len(polymer) < len(smallest_reacted_polymer):
			smallest_reacted_polymer = polymer
			problematic_unit = c
	else:
		smallest_reacted_polymer = polymer
		problematic_unit = c

print (f"There are {len(smallest_reacted_polymer)} units left after removing the problematic unit ({problematic_unit.upper()}/{problematic_unit}) and fully reacting the polymer.")