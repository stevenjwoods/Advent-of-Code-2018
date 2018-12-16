# Steven Woods
# Advent of Code 2018
# Day 1: Chronal Calibration, part 1

current_frequency = 0

frequency_file = "frequency_shifts.txt"
frequency_shifts = open(frequency_file, "r")
for line in frequency_shifts:
	line = int(line.rstrip())
	#print "Current frequency is", current_frequency
	#print "Frequency shift is", line, "\n"
	current_frequency = current_frequency + line
print "The resulting frequency after all the changes in frequency have been applied is {0}.".format(current_frequency)