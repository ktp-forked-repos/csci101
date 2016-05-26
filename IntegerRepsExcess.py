#!/usr/bin/python2
# IntegerRepsExcess.py
# https://csintro.mines.edu/csci101/wiki/PythonAssignments/IntegerRepsExcess

def excessBits(numBits, decNumber):
    bitList = []
    decNumber += pow(2, (numBits-1))

    while decNumber > 0:
        mod = decNumber % 2
        bitList += [mod]
        decNumber = (decNumber - mod) / 2

    bitList.reverse()
    while len(bitList) < numBits:
        bitList = [0] + bitList

    return bitList

def excessValue(excessNumber):
    place = 0
    decNumber = 0 - pow(2, len(excessNumber)-1)
    excessNumber.reverse()

    for i in excessNumber:
        decNumber += i * pow(2, place)
        place += 1

    return decNumber

numBits = input("Enter the number of bits to use: ")
decNumber = input("Enter an integer to encode: ")
print "You entered", numBits, "and", decNumber
excessList = excessBits(numBits, decNumber)
print "The excess representation (LSB last) is", excessList
print "The double-check value is %d." % excessValue(excessList)
