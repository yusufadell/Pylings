#
# Problem:
# Booleans have the following logical operators defined for them:
#
#  &    conditional AND    p & q  results true only if both p and q are true.
#  |    conditional OR     p | q  results true if either p or q are true.
#  !     NOT                !p      results true if p is false.
#
# You may also use equality check `==` and the inequality check `!=` on boolean
# types. The latter emulates the exclusive or operation (XOR).
#
#  !=   comparison NOT EQUAL  p != q  results true if p is not equal to q
#  ==   comparison EQUAL      p == q  results true if p is equal to q
#


def main():
    a = True
    b = False

    # Fix the following line so that
    # it prints out the result of a OR b.
    print(a OR b)
    print(a || b)
    # Fix the following line so that
    # it prints out the result of a AND b.
    print(a AND b)
    print(a && b)


main()
