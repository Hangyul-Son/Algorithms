#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def checkPalindrome(s):
    ascending = list(range(len(s)))
    descending = ascending[::-1]
    for i, j in zip(ascending, descending):
        if s[i] != s[j]:
            return False
    return True

def palindromeIndex(s):
    # Write your code here
    if checkPalindrome(s):
        return -1
    for i in range(len((s))):
        temp_1 = s[:i]
        temp_2 = s[i+1:]
        if checkPalindrome(temp_1+temp_2):
            return i
    return -1
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
    