#!/usr/bin/env python
# import sys because we need to read and write data to STDIN and STDOUT
import sys

sumX = 0
sumY = 0
sumXY = 0
sumXSqr = 0
sumYSqr = 0
n = 0
key = "1"

for line in sys.stdin:
    lst = line.split()
    if lst[0] == key:
        sumX += int(lst[1])
        sumY += int(lst[2])
        sumXY += int(lst[3])
        sumXSqr += int(lst[4])
        sumYSqr += int(lst[5])
        n += int(lst[6])

print("Coefficient of correlation is: ")
#using Pearson's correlation coefficient
numerator = n * sumXY - sumY * sumX

numerator = sumXY - (sumY*(sumX/n)) - (sumX*(sumY/n)) + (n*(sumX/n)*(sumY/n))


deno_part1 = sumXSqr - 2*(sumX/n)*sumX + n * ((sumX/n)**2)
deno_part2 = sumYSqr - 2*(sumY/n)*sumY + n * ((sumY/n)**2)
denominator = deno_part2 * deno_part1
pearson_corr = numerator / (denominator ** 0.5)
print(pearson_corr)



        
