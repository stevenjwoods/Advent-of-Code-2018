# Steven Woods
# Advent of Code 2018
# Day 7: The Sum of Its Parts
# To run: python3 sum_parts.py <path/to/input_file>

import sys
inFile = sys.argv[1]
with open(inFile) as f:
	instructions = f.readlines()

total_steps = dict()
prereq = dict()       # key is prerequisite of (values)
conditions = dict()   # key has prerequisites/conditions of (values)
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
print (f"The correct order of steps is {order}.")


# Part 2:

table = []
header = "\t".join(("Sec", "W1", "W2"))

time_required = dict()
from string import ascii_uppercase
time = 0
for c in ascii_uppercase:
	time += 1
	time_required[c] = time

time = 0
completed_steps = []
time_passed = dict()
for step in order:
	time_passed[step] = int(0)

work_complete = False
prev_line = [str(time), ".", "."]
while work_complete is not True:
	line = [str(time), ".", "."]
	worker_available = False

	for step in order:
		if step not in completed_steps and time_passed[step] == time_required[step]:
			completed_steps += step

	for i in range(1, 3):  # i = 1 and i = 2   (worker columns)
		if line[i] == ".": # If worker is available
			if prev_line[i] != "." and prev_line[i] in completed_steps:  # If previous step completed
				worker_available = True

	for step in order:
		if step not in completed_steps:   # Then begin looking for which step can be worked on next

			if step in conditions:  # If there are prerequisites for the step
				step_unlocked = True

				for prereq in conditions[step]: # If prereqs not yet complete (i.e. step not unlocked)
					if prereq not in completed_steps:
						step_unlocked = False

				for i in range(1, 3):  # i = 1 and i = 2
					if step_unlocked is True and line[i] == ".":  # Left-most available worker found
						if prev_line[i] == "." or prev_line[i] == step or prev_line[i] in completed_steps:  # Ensure worker is ready to move on
							line[i] = step  # Adds step to current worker
							time_passed[step] += 1
						break  # Break out of loop so won't try to add step to additional available workers

			else:	# If there are no prerequisites for the step
				for i in range(1, 3):  # i = 1 and i = 2
					if line[i] == ".":  # Left-most available worker found
						if prev_line[i] == "." or prev_line[i] == step or prev_line[i] in completed_steps:  # Ensure worker is ready to move on
							line[i] = step      # Adds step to current worker
							time_passed[step] += 1
						break  # Break out of loop so won't try to add step to additional available workers
	
	#for l in table:
	#	print(l)
	#print ("\n")
	table.append("\t".join(line))
	prev_line = line
	time += 1

	if len(completed_steps) == len(total_steps):
		print(f"It would take {len(line) - 1} workers {line[0]} seconds to complete all the steps.")
		work_complete = True
		break

print(header)
for line in table:
	print(line)

