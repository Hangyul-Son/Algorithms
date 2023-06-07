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
    return True if s[::-1] == s else False

def palindromeIndex(s):
    # Write your code here
    if checkPalindrome(s):
        return -1
    for i in range(len((s))//2):
        if s[i] != s[len(s)-i-1]:
            temp_1 = s[:i]
            temp_2 = s[i+1:]
            if checkPalindrome(temp_1+temp_2):
                return i
            
            temp_1 = s[:len(s)-i-1]
            temp_2 = s[len(s)-i-1+1:]
            if checkPalindrome(temp_1+temp_2):
                return len(s)-i-1
            
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
