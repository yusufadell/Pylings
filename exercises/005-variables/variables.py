"""
Variables are simply names—created by you or Python—that are used to keep track of
information in your program.

Python's dynamic typing model—that is, the way
that Python keeps track of object types for us automatically, rather than requiring us
to code declaration statements in our scripts.

but in Python:
    • Variables are created when they are first assigned values.
    • Variables are replaced with their values when used in expressions.
    • Variables must be assigned before they can be used in expressions.
    • Variables refer to objects and are never declared ahead of time.

variables: and objects are associated by references in Python;

Variable creation
    A variable (i.e., name), like a, is created when your code first assigns it a value.
    Future assignments change the value of the already created name. Technically,
    Python detects some names before your code runs, but you can think of it as though
    initial assignments make variables.

Variable types
    A variable never has any type information or constraints associated with it. The
    notion of type lives with objects, not names. Variables are generic in nature; they
    always simply refer to a particular object at a particular point in time.

Variable use
    When a variable appears in an expression, it is immediately replaced with the object
    that it currently refers to, whatever that may be. Further, all variables must be
    explicitly assigned before they can be used; referencing unassigned variables results
    in errors

In sum, variables are created when assigned, can reference any type of object, and must
be assigned before they are referenced. This means that you never need to declare names
used by your script, but you must initialize names before you can update them; counters, 
for example, must be initialized to zero before you can add to them.
"""

# 1. Consider the following three statements. Do they change the value printed for A?

A = "spam"
B = A
B = "shrubbery"


# 2. Consider these three statements. Do they change the printed value of A?

A = ["spam"]
B = A
B[0] = "shrubbery"
