#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#
from collections import deque
def solve(arr, queries):
    # Write your code here
    Q = []
    
    for q in queries:
        queue = deque(arr[0:q])
        min_val = max_val = max(queue)
        
        for i in range(q,len(arr)):
            queue.append(arr[i])
            if arr[i] > max_val:
                max_val = arr[i]

            if queue.popleft() == max_val:
                max_val = max(queue)
            
            if max_val < min_val:
                min_val = max_val
        Q.append(min_val)
    return Q
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
