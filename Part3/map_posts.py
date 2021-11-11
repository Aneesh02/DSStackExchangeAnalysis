#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT


import sys
import xml.etree.ElementTree as ET
import re

pattern = re.compile(r'\<(.*?)\>')

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    try:
        root = ET.fromstring(line)
        tags=root.attrib["Tags"]
        for match in pattern.finditer(tags):
            print ("{}\t{}".format(match.group(1),1))
    except Exception:
        pass


        
