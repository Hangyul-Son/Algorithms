#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    
    def blast(grid, height, row):
        temp_grid = [[ 'O' for _ in range(row)] for _ in range(height)]
        for h in range(height):
            for r in range(row):
                if grid[h][r] == 'O':
                    temp_grid[h][r] = '.'
                    if h<height-1:
                        temp_grid[h+1][r] = '.'
                    if r<row-1:
                        temp_grid[h][r+1] = '.'
                    if h>0:
                        temp_grid[h-1][r] = '.'
                    if r>0:
                        temp_grid[h][r-1] = '.'
                        
        return temp_grid
        
    height  = len(grid)
    row = len(grid[0])
    
    temp_grid = [[ 'O' for _ in range(row)] for _ in range(height)]
    
    if n == 1:
        return grid
    if n % 2 == 0:
        return ["".join(i) for i in temp_grid]
    
    grid = blast(grid, height, row)
    grid_2 = blast(grid, height, row)
    if n % 4 == 3: 
        return ["".join(i) for i in grid]
    else:
        return ["".join(i) for i in grid_2]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
