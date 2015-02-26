def ndivisible_digits(nbr_digits, divisor):
    max_int = int('9' * nbr_digits)
    remainder = max_int % divisor
    
    if not remainder:
        return max_int
    elif remainder == max_int:
        return False
    else:
        return max_int - remainder
        
print ndivisible_digits(3,3)
print ndivisible_digits(3,4)
print ndivisible_digits(1,37)
print ndivisible_digits(7,4241275)