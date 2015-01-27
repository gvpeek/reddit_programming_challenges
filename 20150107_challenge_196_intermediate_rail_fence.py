test = {'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG' : 'TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO'}

current_level = 0
direction = 1
depth = 4
rail_fences =[[] for x in xrange(depth)]

for message, result in test.iteritems():
	for char in message:
		rail_fences[current_level].append(char)
		current_level += (1 * direction)
		if current_level == 0:
			direction = 1
		elif current_level == depth - 1:
			direction = -1
print rail_fences