#!/usr/bin/python2
# Collatz.py
# https://csintro.mines.edu/csci101/wiki/PythonAssignments/CollatzConjecture

input = input("Enter a positive integer value: ")
print input,

number = input
count = 1
upcount = 0
downcount = 0

while number > 1:
    count += 1
    if number % 2 == 0:
        number = number / 2
        downcount += 1
    else:
        number = 3 * number + 1
        upcount += 1
    print number,

print "\nHailstone sequence length for", input, "is", count, "with",\
      upcount, "increases and", downcount, "decreases."
