from itertools import chain

test = {'enc 4 THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG' : 'TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO'}

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

    return cipher

def decode(depth, cipher):
    current_level = 0
    direction = 1
    rows =[[] for x in xrange(depth)]
    message_list = ['' for x in xrange(len(cipher))]
    message = '' 
    
    for n in xrange(len(cipher)):
        rows[current_level].append(n)
        current_level += (1 * direction)
        if current_level == 0:
            direction = 1
        elif current_level == depth - 1:
            direction = -1
    order = list(chain.from_iterable(rows))
    
    for enum, position in enumerate(order):
        message_list[position] = cipher[enum]
        
    message = ''.join(message_list)
    
    return message
    

if __name__ == '__main__':
    while True:
        user_input = raw_input('Enter a task ("enc" or "dec"), depth and message: ')
        if user_input == 'exit':
            break
        try:
            task, depth, message = user_input.split()
            if task not in ['enc', 'dec']:
                print 'Please enter a valid task, "enc" or "dec"'
            if not depth.isdigit():
                print 'Depth must be an integer.'
            depth = int(depth)
            if task == 'enc':
                output = encode(depth, message)
            elif task == 'dec':
                output = decode(depth, message)
            
            print output
        except ValueError, e:
            print 'Please enter the correct number of arguments.'
