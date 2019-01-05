# Steven Woods
# Advent of Code 2018
# Day 9: Marble Mania
# To run: python3 marble.py

# 486 players; last marble is worth 70833 points

players = int(input("Enter the number of players: "))
last_marble = int(input("Enter how much the last marble is worth: "))

turn = ["[-]", "(0)"]
output = "\t".join(turn)
print(output)

scores = dict()
for i in range(1, players+1):
	scores[i] = int(0)

marble_location = int(1)
(current_marble, player_number) = (int(1), int(1))
while current_marble <= last_marble:
	turn[0] = "["+str(player_number)+"]"
	turn[marble_location] = turn[marble_location].replace("(", "").replace(")", "")

	if current_marble % 23 is 0:
		marble_location = marble_location - 7
		if marble_location <= 0:
			marble_location = len(turn) + marble_location - 1  # marble_location is negative here
		scores[player_number] += (current_marble + int(turn[marble_location]))
		del turn[marble_location]
		turn[marble_location] = "("+str(turn[marble_location])+")" 
	
	else:
		if len(turn) - marble_location < 2:
			marble_location = 2
			turn.insert(marble_location, "("+str(current_marble)+")")
		elif len(turn) - marble_location is 2:
			turn.append("("+str(current_marble)+")")
			marble_location = len(turn) - 1
		else:
			marble_location += 2
			turn.insert(marble_location, "("+str(current_marble)+")")


	output = "\t".join(turn)
	#print(output)

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