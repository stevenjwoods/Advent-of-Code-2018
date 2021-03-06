# Steven Woods
# Advent of Code 2018
# Day 2: Inventory Management System, part 1
# To run: python3 inventory_management_pt1.py <path/to/input_file>

import sys
inFile = sys.argv[1]

box_count2, box_count3 = 0, 0
with open(inFile, "r") as boxes:
	for box in boxes:
		counts = dict()
		letter_count2, letter_count3 = False, False
		for letter in box:
			if box.count(letter) is 2:
				letter_count2 = True
			if box.count(letter) is 3:
				letter_count3 = True
		if letter_count2 is True:
			box_count2 += 1
		if letter_count3 is True:
			box_count3 += 1

print (f"{box_count2} boxes have two of the same letter and {box_count3} boxes have three of the same letter. Checksum = {box_count2} * {box_count3} = {box_count2 * box_count3}")