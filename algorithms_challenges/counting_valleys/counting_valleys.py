#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    #start
    alt = 0
    hike = [0]
    for step in path:
        if step == 'U':
            alt +=1
        else:
            alt -= 1
        hike.append(alt)
    valleys = ['valley' for i,alt in enumerate(hike[:-1]) if (alt == 0 and hike[i+1]<0)]
    return len(valleys)
    #end
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
