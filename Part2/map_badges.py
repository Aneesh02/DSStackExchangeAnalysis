#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys
import re

pattern = re.compile(r'Name=\"(\w*[ ]?(\w*)?)".*TagBased="(\w*)"')

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    for match in pattern.finditer(line):
        if match.group(3)=="False":
            print ("{}\t{}".format(match.group(1),1))
            

    # we are looping over the words array and printing the word
    # with the count of 1 to the STDOUT
    
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        
