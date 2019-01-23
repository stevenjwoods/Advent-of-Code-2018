# Steven Woods
# Advent of Code 2018
# Day 3: No Matter How You Slice It
# To run: python3 slice.py <path/to/input_file>

import sys
inFile = sys.argv[1]

with open(inFile) as f:
	claims = [x.strip() for x in f.readlines()]

counts = dict()
claim_inches = dict()
for claim in claims:
	claim_inches[claim] = []
	c = claim.replace(":", "").split(" ")
	location, size = c[2].split(","), c[3].split("x")
	x_add, y_add = 1, 1
	while y_add <= int(size[1]):
		while x_add <= int(size[0]):
			inch = str(int(location[0]) + x_add) + "," + str(int(location[1]) + y_add)
			counts[inch] = counts.get(inch, 0) + 1
			claim_inches[claim].append(inch)
			x_add += 1
		x_add = 1  # Reset x
		y_add += 1  # Increment y to move row

overlapping_inches, unique_claim = 0, ()

for inch in counts:
	if counts[inch] > 1:
		overlapping_inches += 1

for claim in claim_inches:
	overlaps = False
	for inch in claim_inches[claim]:
		if counts[inch] > 1:
			overlaps = True
	if overlaps is False:
		unique_claim = claim

print (f"{overlapping_inches} square inches of fabric are within two or more claims.")
print (f"The claim that does not overlap any others is {unique_claim}.")