#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT


from operator import itemgetter
import sys

current_view_count = 0
current_count = 0
view_count = 0
posts=[]

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # spliting the data on the basis of tab we have provided in mapper.py
    view_count, count, post_id = line.split('\t', 2)
    # convert count (currently a string) to int
    try:
        count = int(count)
        view_count=int(view_count)
        post_id=int(post_id)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_view_count == view_count:
        current_count += count
        posts.append(post_id)
    else:
        if current_view_count:
            # write result to STDOUT
            print ('{}\t{}\t{}'.format(current_view_count, current_count,posts))
            posts=[]
        current_count = count
        current_view_count = view_count
        posts.append(post_id)

# do not forget to output the last word if needed!
if current_view_count == view_count:
    print ('{}\t{}\t{}'.format(current_view_count, current_count,posts))


        
