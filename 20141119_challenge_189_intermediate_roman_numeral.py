from collections import OrderedDict
    
def determine_roman_numeral(integer):
    if not 1 <= integer <= 4999:
        print 'Number must be between 1 and 4999.'
        return False
    
    int2num = OrderedDict()
    int2num[1000] = ['M', 4, 900, 'C']
    int2num[500] = ['D', 3, 400, 'C']
    int2num[100] = ['C', 3, 90, 'X']
    int2num[50] = ['L', 3, 40, 'X']
    int2num[10] = ['X', 3, 9, 'I']
    int2num[5] = ['V', 3, 4, 'I']
    int2num[1] = ['I', 3, None, None]
    
    number = integer
    roman_numeral = ''

    for divisor in int2num.keys():
        result = number/divisor
        remainder = number%divisor
    
        if 0 < result <= int2num[divisor][1]:
            roman_numeral += result * int2num[divisor][0]
            number = remainder        
        
        if int2num[divisor][2] and number >= int2num[divisor][2]:
            roman_numeral += int2num[divisor][3] + int2num[divisor][0]
            number -= int2num[divisor][2]
        
    return roman_numeral

def determine_integer(roman_numeral):
    
    num2int = OrderedDict()
    num2int['M'] = 1000
    num2int['D'] = 500
    num2int['C'] = 100
    num2int['L'] = 50
    num2int['X'] = 10
    num2int['V'] = 5
    num2int['I'] = 1
    
    numeral = roman_numeral
    integer = 0
    valid_symbols = num2int.keys()
    
    for char in numeral:
        if not char in valid_symbols:
            print 'Invalid character in roman numeral.'
            return False
    
    for symbol in valid_symbols:
        if numeral:
            while numeral and symbol == numeral[0]:
                integer += num2int[symbol]
                numeral = numeral[1:]
            if len(numeral) > 1:
                if symbol == numeral[1]:
                    if not (num2int[symbol] / num2int[numeral[0]] == 5 or num2int[symbol] / num2int[numeral[0]] == 10):
                           print 'Invalid Roman Numeral structure.'
                           return False
                    integer += num2int[symbol] - num2int[numeral[0]]
                    numeral = numeral[2:]
                    
    return integer
            

def test():
    tests = 0
    success_num = 0
    success_int = 0
    numbers = {
        'IV' : 4,
        'XXXIV' : 34,
        'CCLXVII' : 267,
        'DCCLXIV' : 764,
        'CMLXXXVII' : 987,
        'MCMLXXXIII' : 1983,
        'MMXIV' : 2014,
        'MMMM' : 4000,
        'MMMMCMXCIX' : 4999,
    }

    for k, v in numbers.iteritems():
        tests += 1
        calc_numeral = determine_roman_numeral(v)
        print calc_numeral
        if calc_numeral == k:
            print 'Successful Numeral Test'
            success_num += 1
            
        integer = determine_integer(k)
        print integer
        if integer == v:
            print 'Successful Integer Test'
            success_int += 1
            
    print 'Tests: ', tests, 'Successful Num: ', success_num, 'Successful Int: ', success_int
            
if __name__ == '__main__':
    while True:
        user_input = raw_input('Enter a roman numeral or integer to be converted: ')
        if user_input == 'quit':
            break
        elif user_input == 'test':
            test()
        elif user_input.isdigit():
            roman_numeral = determine_roman_numeral(int(user_input))
            if roman_numeral:
                print roman_numeral
        elif user_input.isalpha():
            integer = determine_integer(user_input)
            if integer:
                print integer