# Steven Woods
# Advent of Code 2018
# Day 2: Inventory Management System, part 1
# To run: python inventory_management_pt1.py <path/to/input_file>

import sys
inFile = sys.argv[1]

(box_count2, box_count3) = (0, 0)
IDs = open(inFile, "r")
for ID in IDs:
	counts = dict()
	ID = ID.rstrip()
	while ID:
		letter = ID[0]  # Look at first letter in string
		counts[letter] = counts.get(letter, 0) + 1  # Count letter
		ID = ID[1:]   # Remove the counted letter from string
	(letter_count2, letter_count3) = (False, False)
	for letter in counts:
		if counts[letter] == 2:
			letter_count2 = True
		if counts[letter] == 3:
			letter_count3 = True
	if letter_count2 is True:
		box_count2 += 1
	if letter_count3 is True:
		box_count3 += 1
IDs.close()

print "{0} boxes have two of the same letter and {1} boxes have three of the same letter. Checksum = {0} * {1} = {2}".format(box_count2, box_count3, box_count2 * box_count3)