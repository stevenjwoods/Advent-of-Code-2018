# Steven Woods
# Advent of Code 2018
# Day 9: The Stars Align
# To run: python3 stars.py <path/to/input.txt>

def find_distance(lights):
	min_x, max_x, min_y, max_y = None, None, None, None
	for position in lights:
		coordinates = position.split(",")
		if min_x is not None:
			if int(coordinates[0]) < min_x:
				min_x = int(coordinates[0])
			if int(coordinates[0]) > max_x:
				max_x = int(coordinates[0])
			if int(coordinates[1]) < min_y:
				min_y = int(coordinates[1])
			if int(coordinates[1]) > max_y:
				max_y = int(coordinates[1])	
		else:
			min_x, max_x, min_y, max_y = int(coordinates[0]), int(coordinates[0]), int(coordinates[1]), int(coordinates[1])
	return(min_x, max_x, min_y, max_y)

def draw_grid(min_x, max_x, min_y, max_y, lights):
	grid = [[" "] * 100 for _ in range (45)]
	for position in lights:
		coordinates = position.split(",")
		x, y = int(coordinates[0]), int(coordinates[1])
		x, y = x - min_x, y - min_y
		grid[y][x] = "#"
	for line in grid:
		output = " ".join(line)
		print(output)


import sys
inFile = sys.argv[1]
with open(inFile) as f:
	initial_lights = f.readlines()
initial_lights = [x.strip() for x in initial_lights]

import re
lights = dict()
for light in initial_lights:
	light = light.replace(" ", "")
	ary = re.split("[<>]", light)
	position, velocity = ary[1], ary[3]
	velocity = velocity.split(",")
	try:
		lights[position].append(velocity)
	except KeyError:
		lights[position] = [velocity]

min_x, max_x, min_y, max_y = find_distance(lights)
# In test and input data, the min vals for x and y are negative - I will ignore potential for them to be positive
x_range, y_range = max_x - min_x + 1, max_y - min_y + 1
x_offset, y_offset = abs(min_x), abs(min_y)
min_x, max_x = min_x + x_offset, max_x + x_offset
min_y, max_y = min_y + y_offset, max_y + y_offset

new_lights = dict()
for position in lights:
	coordinates = position.split(",")
	coordinates = str(int(coordinates[0]) + x_offset) + "," + str(int(coordinates[1]) + y_offset)
	new_lights[coordinates] = lights[position]
lights = new_lights.copy()
new_lights.clear()

user_input, time = (), int(0)
drawn, finished = False, False
while finished is False:
	min_x, max_x, min_y, max_y = find_distance(lights)
	x_range, y_range = max_x - min_x, max_y - min_y
	if x_range < 100 and y_range < 45:
		user_input = input("Press enter to watch the sky: ")
		draw_grid(min_x, max_x, min_y, max_y, lights)
		drawn = True
		print(f"{time} seconds elapsed.\n")
	elif drawn is True:
		finished = True
	
	for position in lights:
		for velocity in lights[position]:
			coordinates = position.split(",")
			coordinates = str(int(coordinates[0]) + int(velocity[0])) + "," + str(int(coordinates[1]) + int(velocity[1]))
			try:
				new_lights[coordinates].append(velocity)
			except KeyError:
				new_lights[coordinates] = [velocity]

	time += 1
	lights = new_lights.copy()
	new_lights.clear()

