input_codes=[
 ''' _  _  _  _  _  _  _  _  _ 
    | || || || || || || || || |
    |_||_||_||_||_||_||_||_||_|
 ''',
 '''                           
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
 ''',
 '''     _  _  _  _  _  _     _ 
     |_||_|| || ||_   |  |  ||_ 
       | _||_||_||_|  |  |  | _|
 '''
]

input_digits=['490067715', '000000000', '2424.5757', '111111111']

display_mapping ={
    1 : (('   '), 
         ('  |'),
         ('  |')),
    2 : ((' _ '), 
         (' _|'),
         ('|_ ')),
    3 : ((' _ '), 
         (' _|'),
         (' _|')),
    4 : (('   '), 
         ('|_|'),
         ('  |')),
    5 : ((' _ '), 
         ('|_ '),
         (' _|')),
    6 : ((' _ '), 
         ('|_ '),
         ('|_|')),
    7 : ((' _ '), 
         ('  |'),
         ('  |')),
    8 : ((' _ '), 
         ('|_|'),
         ('|_|')),
    9 : ((' _ '), 
         ('|_|'),
         (' _|')),
    0 : ((' _ '), 
         ('| |'),
         ('|_|')),
}

digit_mapping={val: key for key, val in display_mapping.iteritems()}

def display_from_digits(digits):
    ''' Translates string of integers to bank formatted output
    '''
    if not digits.isdigit():
        print 'input must be a string of integers'
        return False

    display_rows = [[] for x in xrange(3)]
    
    for digit in digits:
        for ix, line in enumerate(display_mapping[int(digit)]):
            display_rows[ix].append(line)

    for line in display_rows:
        print ''.join(line)

def digits_from_display(display):
    input_rows = display.split('\n') 
    tranpose = [line for line in zip(*input_rows)]
    print input_rows
    print
    print tranpose

for entry in input_digits:
    display_from_digits(entry)
for entry in input_codes:
    digits_from_display(entry)