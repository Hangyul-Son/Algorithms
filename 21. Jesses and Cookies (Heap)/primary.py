#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    
            
    B = []
    for i in A:
        if i<k:
            B.append(i)
        
    sorted_list = sorted(B)
    count = 0
    C = []
    while len(sorted_list)>=2:
        new = sorted_list.pop(0) + sorted_list.pop(0) * 2
        count += 1
        if new<k:
            sorted_list.append(new)
            sorted_list.sort()
        else:
            C.append(new)
    if len(sorted_list) == 1 and len(B) == len(A) and len(C)==0:
        return -1
            
    print("length of last list", sorted_list)
    return count + len(sorted_list)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
