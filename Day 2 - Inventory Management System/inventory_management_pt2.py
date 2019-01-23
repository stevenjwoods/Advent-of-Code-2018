# Steven Woods
# Advent of Code 2018
# Day 2: Inventory Management System, part 2
# To run: python3 inventory_management_pt2.py <path/to/input_file>


def match_test(boxes):
	for box in boxes:
		for other_box in boxes:
			if box != other_box:
				for i in range(len(box)):
					if box[:i] + box[i+1:] == other_box[:i] + other_box[i+1:]:
						print(f"Boxes {box} and {other_box} are matching boxes.")
						return (box[:i] + box[i+1:])


import sys
inFile = sys.argv[1]

with open(inFile, "r") as b:
	boxes = [box.rstrip() for box in b]

common_letters = match_test(boxes)			
print (f"The common letters are {common_letters}.")