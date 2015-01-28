from itertools import chain

tests = {'enc 4 THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG' : 'TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO',
        'enc 2 LOLOLOLOLOLOLOLOLO' : 'LLLLLLLLLOOOOOOOOO',
        'dec 4 TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO' : 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG',
        'dec 7 3934546187438171450245968893099481332327954266552620198731963475632908289907' : '3141592653589793238462643383279502884197169399375105820974944592307816406286'}

def get_order(depth, text):
    current_level = 0
    direction = 1
    rows =[[] for x in xrange(depth)]

    for n in xrange(len(text)):
        rows[current_level].append(n)
        current_level += (1 * direction)
        if current_level == 0:
            direction = 1
        elif current_level == depth - 1:
            direction = -1
    return list(chain.from_iterable(rows))

def encode(depth, message):
    cipher_list = ['' for x in xrange(len(message))]
    cipher = ''

    order = get_order(depth, message)

    for enum, position in enumerate(order):
        cipher_list[enum] = message[position]
        
    cipher = ''.join(cipher_list)

    return cipher

def decode(depth, cipher):
    message_list = ['' for x in xrange(len(cipher))]
    message = '' 
    
    order = get_order(depth, cipher)
    
    for enum, position in enumerate(order):
        message_list[position] = cipher[enum]
        
    message = ''.join(message_list)
    
    return message

def process_input(user_input):
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
        
    return output

if __name__ == '__main__':
    while True:
        user_input = raw_input('Enter a task ("enc" or "dec"), depth and message: ')
        if user_input == 'exit':
            break
        elif user_input == 'test':
            for test, result in tests.iteritems():
                print test, result
                output = process_input(test)
                print 'Test Passed!' if output == result else 'Test Failed!'
            break
        try:
            output = process_input(user_input)
            
            print output
        except ValueError, e:
            print 'Please enter the correct number of arguments.'
