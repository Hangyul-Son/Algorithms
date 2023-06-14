#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    mod = pow(10,9) + 7
    combinations = [1,1,2,4]
    total = [1,1,2**n, 4**n]
    while len(combinations) <= m:
        c = sum(combinations[-4:]) % mod
        combinations.append(c)
        total.append(pow(c,n,mod))
    
    # print('n',n,'m',m)
    sturdy = [1]*(m+1)
    for i in range(2, m+1):
        unstable = 0
        for j in range(1, i):
            unstable += (sturdy[j] * total[i-j])
        # print(i, "unstable", unstable)
        sturdy[i] = total[i]-unstable%mod
        
    return sturdy[-1] % mod
    
        


    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
