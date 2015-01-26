test_cases = ['because cause',
'hello below',
'hit miss',
'rekt pwn',
'combo jumbo',
'critical optical',
'isoenzyme apoenzyme',
'tribesman brainstem',
'blames nimble',
'yakuza wizard',
'longbow blowup']

for test in test_cases:
    left, right = test.split(' ')
    left, right = list(left), list(right)

    common =[]
    for char in reversed(left):
        if char in right:
            left.remove(char)
            right.remove(char)
            common.append(char)
            
    left_score, right_score = len(left), len(right)
    
    print test 
    print 'Common', common 
    print 'Left:', left_score, left, 'Right:', right_score, right
    print 'Left wins!' if left_score > right_score else 'Right wins!' if right_score > left_score else 'Tie!'
    print