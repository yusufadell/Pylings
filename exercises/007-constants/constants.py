#
# Problem:
# In Python constants are just what the name suggests, constant- unchangeable,
# immutable.
# Python supports constant string, numeric, boolean values.
#
# You can't modify or reassign to a constant in Python.
import math


def main():
    # In Python variable names must start with a letter.
    numeber_twenty = 20
    print(math.sin(numeber_twenty))

    ABC = "abc"
    print(ABC)

    SUM = ABC + "tyk"
    print(SUM)

    # Something's wrong here- an attempt to
    # assign to a constant will cause a compiler error.
    # Instead of assigning to an existing constant, declare a new one!

    SUM = SUM + "cheeky addition"
    print(SUM)


main()
