#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT


import sys
import re

repu_pattern = re.compile(r'Reputation="(\d+)"')
id_userid_pattern = re.compile(r'Id="(\d+)"')
postHistory_pattern = re.compile(r'PostHistoryTypeId="(\d+)"')
id_post_pattern = re.compile(r'UserId="(\d+)"')


for line in sys.stdin:
    post_id = postHistory_pattern.search(line)
    if post_id:
        if int(post_id.group(1)) == 2:
            user_id = id_post_pattern.search(line)
            try:
                print("{}\t{}\t{}".format(user_id.group(1), "Answer", 1))
            except AttributeError:
                continue
    else:
        Reputation = repu_pattern.search(line)
        user_id = id_userid_pattern.search(line)
        try:
            print("{}\t{}\t{}".format(user_id.group(1), "Reputation", Reputation.group(1)))
        except AttributeError:
            continue


        
