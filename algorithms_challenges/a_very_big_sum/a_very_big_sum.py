#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    #start
    return reduce(lambda a,b: a+b, ar)
    #end
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
