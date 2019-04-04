#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
poss_digits = string.digits + string.ascii_lowercase
# Jake Shams helped me optimize this function.
poss_dic_dig = {}
for i, d in enumerate(poss_digits):
        poss_dic_dig[d] = i

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    _digits = digits.lower() 
    result = 0
    # TODO: Decode digits from binary (base 2) 
    # TODO: Decode digits from hexadecimal (base 16)
    # TODO: Decode digits from any base (2 up to 36)
    for i, char in enumerate(reversed(_digits)):
        result += (base**i) * poss_dic_dig[char]
    return result
    # return int(digits, base) # 🖕🏼best solution
    
    


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # TODO: Encode number in hexadecimal (base 16)
    # TODO: Encode number in any base (2 up to 36)
    # got my logic in math here: https://www.rapidtables.com/convert/number/decimal-to-hex.html
    q = number # keeps track of the number decreasing
    d = []
    while q > 0:
        r = q % base
        q = q // base
        # q, r = divmod(q, base) <-- 🖕🏼optimized version
        d.append(poss_digits[r]) # converts anything after 10 into it's appropriate character.
    return ''.join(reversed(d))
    



    


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # TODO: Convert digits from any base to any base (2 up to 36)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    elif len(args) == 2:
        print(encode(int(args[0]), int(args[1])))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
