#!/usr/bin/env python

import sys

current_hour = None
current_count = None

for line in sys.stdin:
    hour,count= line.split("\t",1)
    try:
        count = int(count)
        hour = int(hour)
    except ValueError:
        continue

    if current_hour == hour:
        current_count += 1
    else:
        if current_hour:
            print("{}\t{}".format(current_hour, current_count))
        current_hour = hour
        current_count = 1

print("{}\t{}".format(current_hour, current_count))
