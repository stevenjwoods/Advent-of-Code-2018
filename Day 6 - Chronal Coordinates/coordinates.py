# Steven Woods
# Advent of Code 2018
# Day 6: Chronal Coordinates
# To run: python3 coordinates.py <path/to/input_file>

import sys
inFile = sys.argv[1]
with open(inFile) as f:
	coordinates = f.readlines()
coordinates = [x.strip() for x in coordinates]

max_x, max_y = 0, 0
for c in coordinates:
	ary = c.split(", ")
	if int(ary[0]) > max_x:
		max_x = int(ary[0])
	if int(ary[1]) > max_y:
		max_y = int(ary[1])

grid = [["."] * (max_x + 1) for _ in range (max_y + 1)]

locations = dict()
doubles = False
from string import ascii_uppercase
i = 0
for c in coordinates:
	if i > len(ascii_uppercase) - 1:
		i = 0
		doubles = True
	if doubles is True:
		letter = ascii_uppercase[i] + ascii_uppercase[i]
	else:
		letter = ascii_uppercase[i]
	ary = c.split(", ")
	x, y = int(ary[0]), int(ary[1])
	grid[y][x] = letter
	locations[letter] = [x, y]
	i += 1

y_coordinate, x_coordinate = 0, 0
for y in grid:  # For each row in the grid
	for x in y: # For each element in the row
		if x is ".":
			min_distance, closest_letters = (), []
			for letter in locations:
				distance = abs(x_coordinate - locations[letter][0]) + abs(y_coordinate - locations[letter][1])
				if min_distance:
					if distance < min_distance:
						min_distance = distance
						closest_letter = [letter]
					elif distance == min_distance:
						closest_letter.append(letter)
				else:
					min_distance = distance
					closest_letter = [letter]
			if len(closest_letter) is 1:
				grid[y_coordinate][x_coordinate] = closest_letter[0].lower()
		x_coordinate += 1
	x_coordinate = 0
	y_coordinate += 1

counts = dict()
for y in grid:
	for x in y:
		counts[x.lower()] = counts.get(x.lower(), 0) + 1

counts.pop('.', None)
for x in grid[0]:
	counts.pop(x, None)
for x in grid[-1]:
	counts.pop(x, None)
for y in grid:
	counts.pop(y[0], None)
	counts.pop(y[-1], None)

best_location, largest_area = (), 0
for letter in counts:
	if counts[letter] > largest_area:
		largest_area = counts[letter]
		best_location = letter.upper()

print (f"Location {best_location}, with coordinates {locations[best_location]}, has the largest area ({counts[best_location.lower()]}) surrounding it.")
# Part 1 solved



# Part 2:
y_coordinate, x_coordinate, count = 0, 0, 0
for y in grid:
	for x in y:
		total_distance = 0
		for letter in locations:
			distance = abs(x_coordinate - locations[letter][0]) + abs(y_coordinate - locations[letter][1])
			total_distance += distance
		if total_distance < 10000:   # Change this to 32 if using test file
			count += 1
		x_coordinate += 1
	x_coordinate = 0
	y_coordinate += 1

print (f"The region containing all locations which have a total distance to all given coordinates of less than 10000 has a size of {count}.")
	

	