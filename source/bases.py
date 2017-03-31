#!python

import string


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    # TODO: Decode number
    # Digit * Base ^ Index(r-l)
    # print("Base: ", base, " str_num: ", str_num)
    new_num = 0
    for index, digit in enumerate(str_num):
        # print("ord(digit): ", ord(digit))
        # magic number is 87 for lower case alphabetical
        if ord(digit) > 57:
            # print("digit.lower(): ", digit.lower())
            # print("ord(digit.lower()): ", ord(digit.lower()))
            digit = ord(digit.lower()) - 87
        # print("Digit: ", digit)
        power = len(str_num) - (index + 1)
        # print("Power: ", power)
        new_num += int(digit) * (base ** power)
        # print("New_Num:", new_num)

    return new_num


def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    # TODO: Encode number
    # digit % base ** power
    new_num = ''
    power = 0
    while base ** power <= num:
        power += 1
    power -= 1
    # Now, find the remainder for each power to encode digit by digit
    while power >= 0:
        print("Power: ", power)
        digit = num // (base ** power)
        if digit > 9:
            digit = chr(digit + 87)
        print("Digit: ", digit)
        num = num % (base ** power)
        power = power - 1
        new_num += str(digit)
        print("new_num: ", new_num)
    return new_num



def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number
    return(encode(decode(str_num, base1), base2))


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
