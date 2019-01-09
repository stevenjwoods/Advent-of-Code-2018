# Steven Woods
# Advent of Code 2018
# Day 9: Marble Mania
# To run: python3 marble.py

# This gets very slow with a large number of marbles (millions). Didn't manage to speed up the process.

players = int(input("Enter the number of players: "))
last_marble = int(input("Enter how much the last marble is worth: "))
part = int(input("Enter which part of the task (1 or 2): "))
if part is 2:
	last_marble = last_marble * 100
	print(f"The number of the last marble has been multiplied by 100, and is now {last_marble}.")
# Should have something to prevent invalid input

turn = [int(0)]

scores = dict()
for i in range(1, players+1):
	scores[i] = int(0)

marble_location = int(0)
(current_marble, player_number) = (int(1), int(1))
while current_marble <= last_marble:
	print(current_marble)

	if current_marble % 23 is 0:
		marble_location = marble_location - 7
		if marble_location <= 0:
			marble_location = len(turn) + marble_location  # marble_location is negative here
		scores[player_number] += (current_marble + turn[marble_location])
		del turn[marble_location]

	else:
		if len(turn) - marble_location < 2:
			marble_location = 1
			turn.insert(marble_location, current_marble)
		elif len(turn) - marble_location is 2:
			turn.append(current_marble)
			marble_location = len(turn) - 1
		else:
			marble_location += 2
			turn.insert(marble_location, current_marble)

	# Prepare for next iteration
	current_marble += 1
	player_number += 1
	if player_number > players:
		player_number = 1

high_score = int(0)
for player in scores:
	if scores[player] > high_score:
		high_score = scores[player]

print(f"{players} players; last marble is worth {last_marble} points: high score is {high_score}.")