#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    rank = [0] * len(ranked)
    result = [0] * len(player)
    
    rank[0] = 1
    
    for i in range(1, len(ranked)):
        if ranked[i] == ranked[i-1]:
            rank[i] = rank[i-1]
        else:
            rank[i] = rank[i-1]+1
    
    print(rank)
    
    for i in range(len(player)):
        for j in reversed(range(len(ranked))):
            if ranked[j] > player[i]:
                result[i] = rank[j] + 1 
                break
            elif ranked[j] == player[i]:
                result[i] = rank[j]
                break
            elif ranked[j] < player[i]:
                result[i] = rank[j] 
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
