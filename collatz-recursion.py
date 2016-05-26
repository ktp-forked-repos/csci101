#!/usr/bin/python2
## CollatzRecursion


###
# define your RECURSIVE version of Collatz below this comment so that it runs
# correctly when called from below.
#
# REQUIREMENTS:
#  a) The correct sequence must be printed, all the values on one line.
#  b) Your Collatz function must use recursion.
#  c) Aside from two arguments accepting a positive integer value and the letter
#     F, B, or P; your Collatz function MAY NOT use any other internal variables.
#  d) Your Collatz function may accept only the two arguments described in (c).
#  e) If the second argument is 'F', the sequence should b printed in its
#       naturally generated order.                        ^
#     If the second argument is 'B', the sequence should be printed in reverse.
#     If the second argument is 'P', then a palindrome of the sequence values should 
#       be printed (see http://en.wikipedia.org/wiki/Palindrome).  In this case
#       it doesn't matter if your function prints the first value as 1 or the
#       value provided by the user.
###

def Collatz( number, displaymode ):
    if displaymode in ['F', 'P']:
        print number,

    if number > 1:
        if number % 2 == 0:
            Collatz( number / 2, displaymode )
        else:
            Collatz( 3 * number + 1, displaymode )

    if displaymode == 'B':
        print number,
    elif displaymode == 'P' and number != 1:
        print number,

    return

###
# Do NOT alter Python code below this line
###
m = input( "Enter a positive integer value: " )
displaymode = ''  # initialize to anything not F, B, P
while displaymode not in ['F', 'B', 'P'] :
    displaymode = raw_input( "Choose a display mode:  F=forward, B=backward, P=palindrome: " )

Collatz( m, displaymode )
print 
