#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT


import sys
import re
CreationDate = re.compile(r'CreationDate="(\d{4})-(\d{2})-(\d{2})T(\d{2}):\d{2}:\d{2}')

for line in sys.stdin:
    matches = CreationDate.search(line)
    try:
        print("{}\t{}".format((matches.group(4)), 1))
    except Exception:
        continue



        
