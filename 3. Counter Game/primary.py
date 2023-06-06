#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
def powerOfTwo(n):
    while n != 1:
        if n % 2 != 0:
            return False
        n = n / 2
    return True
    
def findPowerOfTwo(n):
    count = 0
    while n != 1:
        n = n // 2
        count = count + 1
    return pow(2,count)
    
def counterGame(n):
    # Write your code here
    louise_turn = True
    
    while True:
        if powerOfTwo(n):
            n = n/2
        else:
            n = n - findPowerOfTwo(n)
        
        if n == 1:
            return "Louise" if louise_turn else "Richard"
        louise_turn = False if louise_turn else True
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
