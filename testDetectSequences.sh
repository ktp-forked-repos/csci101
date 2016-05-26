#!/bin/bash
for file in DetectSequences/*.txt; do
    /bin/cp -v "$file" sequences.txt
#    dos2unix sequences.txt
#    sed -i 's/^0*7$/\0/g' sequences.txt
    python2 DetectSequences.py
done
rm sequences.txt
