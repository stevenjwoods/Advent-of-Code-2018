# Steven Woods
# Advent of Code 2018
# Day 11: Chronal Charge
# To run: python3 charge.py


def find_power(row_idx, col_idx):
	row_idx += 1
	col_idx += 1
	rack_id = col_idx + 10
	power_level = (rack_id*row_idx + serial_number) * rack_id
	try:
		hundreds = int(str(power_level)[-3])
	except IndexError:
		hundreds = int(0)
	power_level = hundreds - 5
	return power_level


min_square = int(input("Enter minimum square size: "))
max_square = int(input("Enter maximum square size: "))
serial_number = int(input("Please enter the grid serial number: "))
grid = [[None] * 300 for num in range (300)]
for row_idx in range(len(grid)):
	for col_idx in range(len(grid[0])):
		power_level = find_power(row_idx, col_idx)
		grid[row_idx][col_idx] = power_level

power_sums = dict()
for row_idx in range(len(grid)):
    print(f"Counting squares originating from cells in row {row_idx}...")
    for col_idx in range(len(grid[0])):  # For each cell co-ordinate
        power_sum = 0
        
        for square_len in range(1, max_square + 1):  # For every size of square
            if square_len > len(grid) - row_idx or square_len > len(grid[0]) - col_idx:
                break
            for row_offset in range(square_len):
                power_sum += grid[row_idx + row_offset][col_idx + square_len - 1]  # To get right-most cells of square
            for col_offset in range(square_len):
                power_sum += grid[row_idx + square_len - 1][col_idx + col_offset]  # To get bottom cells of square
            power_sum -= grid[row_idx + square_len - 1][col_idx + square_len - 1]  # Remove val of BR as added twice
            tl_coords = str(col_idx + 1) + "," + str(row_idx + 1)

            if square_len >= min_square:
                try:
                    power_sums[tl_coords][square_len] = power_sum
                except KeyError:
                    power_sums[tl_coords] = {square_len: power_sum}

largest_sum, chosen = (), ()
for cell in power_sums:
	for square_len in power_sums[cell]:
		try:
			if power_sums[cell][square_len] > largest_sum:
				largest_sum = power_sums[cell][square_len]
				chosen = [cell, square_len]
		except TypeError:
			largest_sum = power_sums[cell][square_len]
			chosen = [cell, square_len]

cell, square_len = chosen
print(f"""
The chosen square is {square_len}x{square_len}.
The coordinates of the top-left cell are {cell}.
The total power level is {largest_sum}.
""")

# For printing the chosen square:

#col_idx, row_idx = cell.split(",")
#col_idx = int(col_idx) - 1
#row_idx = int(row_idx) - 1
#for row in range(row_idx, row_idx + square_len):
#	for col in range(col_idx, col_idx + square_len):
#		print(grid[row][col], end = "\t")
#	print("\n")
