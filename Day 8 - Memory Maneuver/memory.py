# Steven Woods
# Advent of Code 2018
# Day 7: Memory Maneuver
# To run: python3 memory.py <path/to/input_file>

def make_family(child_quant, existing_nodes_count, child_counter, node_families):    # Fill in child node IDs to make family
	if int(child_quant) > 0:
		for child_number in range(int(child_quant)):
			existing_nodes_count += 1
			child_node_id = ()
			if existing_nodes_count > len(ascii_uppercase):
				index = existing_nodes_count
				count = int(1)
				while index > len(ascii_uppercase):
					index = index - 26
					count += 1
				child_node_id = (ascii_uppercase[index - 1] * int(count))
			else:
				child_node_id = ascii_uppercase[existing_nodes_count - 1]
			child_counter[child_node_id] = int(0)
			node_families[node_id].append(child_node_id)   # Fill in node IDs for family (+= splits str?)
	return existing_nodes_count, child_counter, node_families



import sys
inFile = sys.argv[1]
with open(inFile) as f:
	license = f.read()

numbers = license.split(" ")

from string import ascii_uppercase

nodes = dict()    # Stores header and metadata under node ID.
node_families = dict()   # Stores child IDs under parent ID.
child_counter = dict()  # Counts how many children have been intialised under node
existing_nodes_count = 1   # Tracks the number of nodes and used to assign ID from alphabet.
lineage = []

node_id = ascii_uppercase[0]   # Starts with first node as A
child_counter[node_id] = int(0)
lineage.append(node_id)
header, numbers = numbers[:2], numbers[2:]   # Remove first two nums and store as header for current node
child_quant, metadata_quant = header
nodes[node_id] = header
node_families[node_id] = []
existing_nodes_count, child_counter, node_families = make_family(child_quant, existing_nodes_count, child_counter, node_families)

while numbers:
	added_child = False

	if int(nodes[node_id][0]) > 0:
		parent_node_id = node_id
		parent_child_quant = child_quant
		nodes[node_id][0] = int(nodes[node_id][0]) - 1  # Reduce number of children to go
		node_id = node_families[parent_node_id][child_counter[parent_node_id]]
		child_counter[parent_node_id] += 1    # Increase number of children initialised
		lineage.append(node_id)
		header, numbers = numbers[:2], numbers[2:]
		child_quant, metadata_quant = header
		nodes[node_id] = header
		node_families[node_id] = []
		existing_nodes_count, child_counter, node_families = make_family(child_quant, existing_nodes_count, child_counter, node_families)
		added_child = True

	if (int(nodes[node_id][0]) is 0):
		if (len(nodes[node_id]) is 2):
			nodes[node_id] += numbers[:int(nodes[node_id][1])]
			numbers = numbers[int(nodes[node_id][1]):]
			if added_child is True:
				lineage = lineage[:len(lineage) - 1]
			node_id = lineage[-1]
		else:
			lineage = lineage[:len(lineage) - 1]
			node_id = lineage[-1]

metadata_count = int(0)
for node in nodes:
	nodes[node][0] = child_counter[node]
	for m in nodes[node][2:]:
		metadata_count += int(m)

print (f"The sum of all metadata entries is {metadata_count}.")


# Part 2:

root_value = int(0)
references = dict()
lineage = []
node_id = 'A'
lineage.append(node_id)
references[node_id] = nodes[node_id][2:]
complete = False
while complete is not True:
	if not references['A'] and len(lineage) is 1:
		complete = True
	else:
		if references[node_id]:   # If there are still metadata entries (references)
			child_node_ref, references[node_id] = references[node_id][0], references[node_id][1:]
			if child_counter[node_id] > 0:   # If the node has children (metadata become references)
				if int(child_node_ref) <= len(node_families[node_id]):   # If referenced child exists
					node_id = node_families[node_id][int(child_node_ref) - 1]
					lineage.append(node_id)
					references[node_id] = nodes[node_id][2:]

			else:  # If the node has NO children (metadata values get added to root value)
				for m in nodes[node_id][2:]:
					root_value += int(m)
				lineage = lineage[:len(lineage) - 1]
				node_id = lineage[-1]

		else: 	# If there are no more metadata entries (references)
			lineage = lineage[:len(lineage) - 1]
			node_id = lineage[-1]

print (f"The value of the root node 'A' is {root_value}.")


