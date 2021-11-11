#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT


import sys
import xml.etree.ElementTree as ET
import re



# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    try:
        root = ET.fromstring(line)
        view_count=root.attrib["ViewCount"]
        post_id=root.attrib["Id"]

        print ("{}\t{}\t{}".format(view_count,1,post_id))
    except Exception:
        pass


        
