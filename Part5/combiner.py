#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT

import sys

current_user_id= None
current_repu = None
current_ans= 0


sumX = 0
sumY = 0
sumXY = 0
sumXSqr = 0
sumYSqr = 0
n = 0


for line in sys.stdin:
    temp = line.split("\t")
    user_id = temp[0]
    word = temp[1]
    count = int(temp[2])

    if user_id == current_user_id:
        if word == "Reputation":
            current_repu = count
        else:
            current_ans+= 1

    else:
        if current_user_id:
            sumX += current_repu
            sumY += current_ans
            sumXY += current_repu * current_ans
            sumXSqr += current_repu * current_repu
            sumYSqr += current_ans* current_ans
            n += 1
        if word == "Reputation":
            current_repu = count
            current_ans= 0
        else:
            current_ans= 1
            current_repu = None
        current_user_id= user_id

sumX += current_repu
sumY += current_ans
sumXY += current_repu * current_ans
sumXSqr += current_repu * current_repu
sumYSqr += current_ans* current_ans
n += 1

print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format("1", sumX, sumY, sumXY, sumXSqr, sumYSqr, n))
