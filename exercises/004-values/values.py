#
# Problem:
# Python is a dynamicaly, strongly typed language:
#  - All values in python have a defined type at run time (dynamic typing)
#  - Operations between values of different types is not allowed (strong typing)
#
# Operations can only be done with values of the same type.
#
# This also means a type coercion does not happen in python. For example: You can't
# add a boolean to a number without converting it with a function first.
#


def main():
    # Oops! Looks like someone wanted to add 2.7 to Pi but
    # typed it in as a string. Change 2.7 to be a number so
    # that the result of 3.14159 plus 2.7 is printed.
    print(3.14159 + "2.7")


if __name__ == "__main__":
    main()
