# Steven Woods
# Advent of Code 2018
# Day 2: Inventory Management System, part 2
# To run: python inventory_management_pt2.py <path/to/input_file>

import sys
inFile = sys.argv[1]

boxes = []
b = open(inFile, "r")
for box in b:
	box = box.rstrip()
	boxes.append(box)
b.close()

matching_pair = []
for box in boxes:
	if not matching_pair:
		matches = dict()
		i = 0
		while i < len(box):
			matches[i] = []
			for other_box in boxes:   # NB each box also compared to self
				if other_box[i] == box[i]:
					matches[i].append(other_box)	# Store IDs with common letter at that position
			i += 1
		counts = dict()
		for letter_pos in matches:
			for other_box in matches[letter_pos]:
				counts[other_box] = counts.get(other_box, 0) + 1
		for other_box in counts:
			if counts[other_box] == len(box) - 1:
				print "Boxes {0} and {1} are the correct boxes.".format(box, other_box)
				matching_pair = (box, other_box)

i = 0
while matching_pair[0][i] == matching_pair[1][i]:
	i += 1
common_letters = matching_pair[0][0:i] + matching_pair[0][i+1:]   # Removes the mismatch

print "The common letters are {0}.".format(common_letters)