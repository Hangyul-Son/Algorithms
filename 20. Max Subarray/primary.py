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
    max_subarray = arr[0]
    temp = 0
    
    if max(arr) >= 0:
        max_subsequence = 0
        for i in arr:
            if i > 0:
                max_subsequence += i
    else:         
        max_subsequence = arr[0]
        for i in arr:         
            if i > max_subsequence:
                max_subsequence = i
    for i in arr:         
        if (temp + i) >= i:
            temp += i
        else:
            temp = i
        if temp >= max_subarray:
            max_subarray = temp
    
    return [max_subarray, max_subsequence]
            
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
