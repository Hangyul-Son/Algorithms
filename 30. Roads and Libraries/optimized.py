#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_road >= c_lib:
        return n*c_lib
    
    total_city = set()
    dp = [[i] for i in range(n+1)]
    
    for [x,y] in cities:
        # total_city.add(x)
        # total_city.add(y)
        if id(dp[x]) != id(dp[y]):
            for i in dp[y]:
                dp[x].append(i)
                dp[i] = dp[x]
                
    num_groups = len(set([id(group) for group in dp[1:]]))
    # num_groups = num_groups + n - len(total_city)
    
    return num_groups * c_lib + (n-num_groups) * c_road 
    
                
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
 
