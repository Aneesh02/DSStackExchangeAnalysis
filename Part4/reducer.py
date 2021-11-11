#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys

current_month = ""
current_comment_number = 0
word = ""
arry = []
dic = {}

for line in sys.stdin:
    month, comment_len = line.split("\t", 1)
    try:
        length = int(comment_len)
    except ValueError:
        continue

    if current_month == month:
        current_comment_number += 1
        dic[length] = dic.get(length,0) + 1
    else:
        if current_month:
            sorted_dict = dict(sorted(dic.items()))
            count = sum(sorted_dict.values())
            middle = count // 2
            temp = 0
            for key,value in sorted_dict.items():
                temp += value
                if temp >= middle:
                    median = key
                    break   
            print("{}\t{}\t{}".format(current_month, current_comment_number, median))
        current_comment_number = 1
        current_month = month
        array = [length]
        dic = {}

sorted_dict = dict(sorted(dic.items()))
count = sum(sorted_dict.values())
middle = count // 2
temp = 0
for key,value in sorted_dict.items():
    temp += value
    if temp >= middle:
        median = key
        break   

print("{}\t{}\t{}".format(current_month, current_comment_number, median))



        
