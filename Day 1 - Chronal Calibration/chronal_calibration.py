# Steven Woods
# Advent of Code 2018
# Day 1: Chronal Calibration
# To run: python3 chronal_calibration.py <path/to/frequency_shift_file>

import sys
inFile = sys.argv[1]

frequency_shifts = []
f = open(inFile, "r")
for change in f:
	change = int(change.rstrip())
	frequency_shifts.append(change)
f.close()
# frequency_shifts is a list containing all the changes in frequency as integers

(current_frequency, first_round, calibrated) = (0, (),())  
counts = dict()
while not calibrated:    # Until the same number (frequency) is seen twice, the next change in the list is applied
	for change in frequency_shifts:
		counts[current_frequency] = counts.get(current_frequency, 0) + 1
		if counts[current_frequency] == 2:	# The same number (frequency) has been seen twice - device is calibrated
			calibrated = current_frequency  # The frequency at calibration is stored for later output
			break
		current_frequency += change
	if not first_round:						# Frequency after one iteration through list of changes is stored for output.
		first_round = current_frequency

print (f"The resulting frequency after all the changes in frequency have been applied is {first_round}.")
print (f"The first frequency to be reached twice when the changes are repeated is {calibrated}.")