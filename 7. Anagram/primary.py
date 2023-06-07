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
    
    alphabet_set = set(list(s))
    
    first_half_dict = {}
    second_half_dict = {}
    
    for i in alphabet_set:
        first_half_dict[i] = 0
        second_half_dict[i] = 0
    
        first_half_list = s[0:int(len(s)/2)]
    second_half_list = s[int(len(s)/2):]
    
    for i in first_half_list:
        first_half_dict[i] = first_half_dict[i]+1
    for i in second_half_list:
        second_half_dict[i] = second_half_dict[i]+1
    
        change = 0
    for i in alphabet_set:
        change = change + abs(first_half_dict[i] - second_half_dict[i])/2
    return int(change)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
