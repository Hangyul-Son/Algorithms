#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    arr_sum = sum(arr)
    temp = 0
    for i in range(len(arr)):
        if temp == (arr_sum - arr[i])/2:
            return "YES"
        elif temp > (arr_sum - arr[i])/2:
            return "NO"
        temp = temp + arr[i]  
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')