#!/usr/bin/python2
# DetectSequences.py
# https://csintro.mines.edu/csci101/wiki/PythonAssignments/DetectSequence

sequenceFile = file("sequences.txt", "r")
a = 3
epsilon = 7
seqLen = 0
founda = False
terminated = False
escpaed = False

while True:
    line = sequenceFile.readline()
    if len(line) == 0:
        break

    xi = int(line)
    if xi == a:
        seqLen += 1
        if founda == False:
            founda = True
        elif not escaped:
            terminated = True
            break
        escaped = False

    elif founda:
        seqLen += 1
        if xi == epsilon and not escaped:
            escaped = True
        else:
            escaped = False

if seqLen > 0 and terminated:
    print "Accept", seqLen
else:
    print "BOGUS"
