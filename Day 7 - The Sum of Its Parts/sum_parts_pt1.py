# Steven Woods
# Advent of Code 2018
# Day 7: The Sum of Its Parts, part 1
# To run: python sum_parts_pt1.py <path/to/input_file>

import sys
inFile = sys.argv[1]
with open(inFile) as f:
	instructions = f.readlines()

total_steps = dict()
prereq = dict()
conditions = dict()
for line in instructions:
	ary = line.split(" ")
	if ary[1] in prereq:
		prereq[ary[1]].append(ary[7])
	else:
		prereq[ary[1]] = [ary[7]]
	if ary[7] in conditions:
		conditions[ary[7]].append(ary[1])
	else:
		conditions[ary[7]] = [ary[1]]
	total_steps[ary[1]] = 1
	total_steps[ary[7]] = 1


available_steps = []      # This block finds the first available step
for s in total_steps:
	if s not in conditions:  # If they don't have prerequisites
		available_steps += s
available_steps.sort()
next_step = available_steps[0]

order = [next_step]  
while len(order) < len(total_steps):
	available_steps = available_steps[1:]
	for s in prereq[next_step]:
		available = True
		for c in conditions[s]:
			if c not in order:
				available = False
		if available is True:
			available_steps += s
	if len(available_steps) > 1:
		while len(available_steps) > 0:
			available_steps.sort()
			next_step = available_steps[0]
			order += next_step
			if len(order) == len(total_steps):
				break
			available_steps = available_steps[1:]
			for s in prereq[next_step]:
				available = True
				for c in conditions[s]:
					if c not in order:
						available = False
				if available is True:
					available_steps += s
	else:
		next_step = available_steps[0]
		order += next_step

order = ''.join(order)
print "The correct order of steps is {0}.".format(order)