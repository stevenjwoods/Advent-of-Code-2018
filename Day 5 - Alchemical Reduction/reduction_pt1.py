# Steven Woods
# Advent of Code 2018
# Day 5: Alchemical Reduction part 1
# To run: python3 reduction_pt1.py <path/to/input_file>

import sys
inFile = sys.argv[1]
with open(inFile) as f:
	polymer = f.read()
polymer.strip()

destroyed = ['0']
i = 0
while destroyed:
	destroyed = []
	while i < len(polymer) - 1:
		if polymer[i].lower() == polymer[i+1].lower():
			if (polymer[i].isupper() and polymer[i+1].islower()) or (polymer[i].islower() and polymer[i+1].isupper()):
#				print (f"Unit {polymer[i]} and unit {polymer[i+1]} are of opposite polarity.")
				destroyed = [polymer[i], polymer[i+1]]
				polymer = polymer.replace("{0}{1}".format(polymer[i], polymer[i+1]), "")
		i += 1
	i = 0

print (f"After fully reacting the polymer, there are {len(polymer)} units left.")