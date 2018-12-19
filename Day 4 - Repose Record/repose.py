# Steven Woods
# Advent of Code 2018
# Day 4: Repose Recpord
# To run: python repose.py <path/to/file>

import sys
inFile = sys.argv[1]
with open(inFile) as f:
	records = f.readlines()
records = [x.strip() for x in records]
list.sort(records)

sleep_duration = dict()
sleep_minutes = dict()
guard = sleep_time = wake_time = ()
for r in records:
	if "begins shift" in r:
		ary = r.split(" ")
		for element in ary:
			if "#" in element:
				guard = element
				sleep_minutes[guard] = []

for r in records:
	if "begins shift" in r:
		ary = r.split(" ")
		for element in ary:
			if "#" in element:
				guard = element
	else:
		ary = r.split(":")
		ary = ary[1].split("]")
		if "sleep" in ary[1]:
			sleep_time = int(ary[0])
		elif "wake" in ary[1]:
			wake_time = int(ary[0])
			duration = wake_time - sleep_time
			sleep_duration[guard] = sleep_duration.get(guard, 0) + duration
			while sleep_time < wake_time:
				sleep_minutes[guard].append(sleep_time)
				sleep_time += 1
		else:
			sys.exit("Error: unexpected record format.")

sleepiest_guard = ()
max_sleep = 0
for guard in sleep_duration:
	if sleep_duration[guard] > max_sleep:
		max_sleep = sleep_duration[guard]
		sleepiest_guard = guard
counts = dict()
mode = ()
freq = 0
for minute in sleep_minutes[sleepiest_guard]:
	counts[minute] = counts.get(minute, 0) + 1
for minute in counts:
	if counts[minute] > freq:
		freq = counts[minute]
		mode = minute
print "The sleepiest guard is {0}. He slept for {1} minutes. He was asleep most often at 00:{2}.".format(sleepiest_guard, max_sleep, mode)

(sleepiest_minute, next_sleepiest_minute, sleepiest_guard2) = ((), (), ())
highest_num_times_asleep = 0
for guard in sleep_minutes:
	if sleep_minutes[guard]:
		counts = dict()
		for minute in sleep_minutes[guard]:
			counts[minute] = counts.get(minute, 0) + 1
		num_times_asleep = 0
		for minute in counts:
			if counts[minute] > num_times_asleep:
				num_times_asleep = counts[minute]
				next_sleepiest_minute = minute
		if counts[next_sleepiest_minute] > highest_num_times_asleep:
			highest_num_times_asleep = counts[next_sleepiest_minute]
			sleepiest_minute = next_sleepiest_minute
			sleepiest_guard2 = guard

print "Guard {0} is most frequently asleep on the same minute. He was asleep at 00:{1} a total of {2} times.".format(sleepiest_guard2, sleepiest_minute, highest_num_times_asleep)
