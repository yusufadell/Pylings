#
# Problem:
# This program prints out `hello world` but as of now throws a compiler error
# claiming SyntaxError: invalid syntax. This is because python stops 
# treating print as a keyword in earlier versions, python2: print "Hello World" works perfectly

# Since we  adopts python3 which makes it change slightly to print as a function
# argument of any type the languge supports displayed in console.

# scaping characters have their special meaning e.g /n means a new line printed out

# want to use a more  structued way for displaying data
# check out pprint.pprint as => from pprint import pprint 
# which is highly customizable that the usual print statement. 

def main():
    print "Hello World"
