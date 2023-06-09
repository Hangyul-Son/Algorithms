#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    num = []
    
    for c in set(s):
        num.append(s.count(c))
    
    n = len(num)
    mx = max(num)
    mn = min(num)
    
    if mx * (n -1) + mn == len(s) or mn * n +1 == len(s):
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
