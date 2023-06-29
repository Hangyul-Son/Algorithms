#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    if n == 1 and k >= 1:
        return '9'
    S = list(s)
    B = S.copy()
    start = 0; end = n-1; cnt = 0
    while start < end:
        if S[start] != S[end]:
            S[start] = S[end] = max(S[start], S[end])
            cnt += 1
        start += 1; end -= 1
    if cnt > k:
        return '-1'
    k -= cnt
    start = 0; end = n-1
    while k > 0 and start <= end:
        if S[start] != '9':
            if B[start] != B[end]:
                S[start] = S[end] = '9'
                k -= 1
            elif k > 1:
                S[start] = S[end] = '9'
                k -= 2
            elif start == end:
                S[end] = '9'
                k -= 1
        start += 1; end -= 1
    return ''.join(S)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
