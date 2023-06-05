#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    n = int(n)
    first = True
    while n >= 10: 
        temp = 0
        while n > 0:
            temp = temp + n % 10
            n = n//10
        if first:
            n = temp * k
            first = False 
        else: 
            n = temp
    return n
  
if __name__ == '__main__':    
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)