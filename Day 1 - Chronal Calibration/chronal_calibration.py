# Steven Woods
# Advent of Code 2018
# Day 1: Chronal Calibration

frequency_shifts = []
frequency_file = "frequency_shifts.txt"
for change in open(frequency_file, "r"):
	change = int(change.rstrip())
	frequency_shifts.append(change)

(current_frequency, first_round, calibrated) = (0, (),())
counts = dict()
while not calibrated:
	for change in frequency_shifts:
		counts[current_frequency] = counts.get(current_frequency, 0) + 1
		if counts[current_frequency] == 2:
			calibrated = current_frequency
			break
		current_frequency += change
	if not first_round:
		first_round = current_frequency

# 77271 solution
print "The resulting frequency after all the changes in frequency have been applied is {0}.".format(first_round)
print "The first frequency to be reached twice when the changes are repeated is {0}.".format(calibrated)