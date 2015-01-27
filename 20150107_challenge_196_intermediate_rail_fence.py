test = {'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG' : 'TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO'}

def encode(depth, message):
	current_level = 0
	direction = 1
	rows =[[] for x in xrange(depth)]
	cipher = ''

	for char in message:
		rows[current_level].append(char)
		current_level += (1 * direction)
		if current_level == 0:
			direction = 1
		elif current_level == depth - 1:
			direction = -1
	for row in rows:
		for char in row:
			cipher += char
	print cipher
	

if __name__ == '__main__':
    while True:
    	user_input = raw_input('Enter a task ("enc" or "dec"), depth and message: ')
    	try:
	    	task, depth, message = user_input.split()
	    	if task not in ['enc', 'dec']:
	    		print 'Please enter a valid task, "enc" or "dec"'
	    	if not depth.isdigit():
	    		print 'Depth must be an integer.'
	    	depth = int(depth)
	    	encode(depth, message)
    	except ValueError, e:
    		print 'Please enter the correct number of arguments.'
