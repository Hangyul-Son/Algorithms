#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    count = 0
    for i in range(len(q)):
        temp = 0
        
            
    for i in range(len(q)):
        temp = 0
        if q[i] > i+1:
            if q[i] - (i+1) <=2 :
                count = count + q[i]-(i+1)
            else:
                return "Too chaotic"
        else:
            for j in range(i):
                if q[j] > q[i]:
                    temp = temp + 1
            count = count + q[i] + temp - (i+1)
    return count 
    
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        result = minimumBribes(q)
        fptr.write(str(result)+'\n')
    

    fptr.close()
