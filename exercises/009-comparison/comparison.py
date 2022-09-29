#
# Problem:
# Python has comparison operators which compare two values and yield a boolean value.
#
# Python has support for the following comparison operators:
#     a == b   means "a equals b"
#     a < b    means "a is less than b"
#     a > b    means "a is greater than b"
#     a != b   means "a does not equal b"
#     a <= b   means "a is less-or-equal than b"
#     a >= b   means "a is greater-or-equal than b"


def main():
    number = 20

    # % is the modulo operator. It returns the remainder of the division.
    # A number is even when the remainder of number/2 is zero.
    reminder = number % 2

    # Something is wrong with this comparison.
    is_even = reminder = 0

    # This should print "20 is even:" followed by true or false depending
    # on whether 20 (the number variable) is really a even number.
    print(number, "is even: ", is_even)


main()
