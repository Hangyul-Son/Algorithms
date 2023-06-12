#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here

    total = best = temp =  0 
    for i in arr:         
        if i>0:
            total += i
    
        temp = max(0, temp + i)
        best = max(temp, best)
    
    if total == 0:
        max_subarray = max_subsequence = max(arr)
    else: 
        max_subsequence = total
        max_subarray = best

    return max_subarray, max_subsequence
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
