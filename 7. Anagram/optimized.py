#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s)%2 == 1:
        return -1
        
    first_half_list = s[0:int(len(s)/2)]
    second_half_list = s[int(len(s)/2):]
    
    count = 0
    for c in list(set(first_half_list)):
        if first_half_list.count(c) > second_half_list.count(c):
            count = count + first_half_list.count(c) - second_half_list.count(c)
    
    return int(count)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
