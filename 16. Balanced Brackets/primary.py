#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    code = pairs.values()
    for c in list(s):
        if c in code:
            stack.append(c)
        elif len(stack) != 0 and pairs[c] == stack.pop():
            pass
        else:
            return "NO"    
    if len(stack) != 0:
        return "NO"
    else:
        return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
