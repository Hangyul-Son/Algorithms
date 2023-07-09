#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#        
def find_end(grid, startX, startY):
    tempx, tempy = startX,startY
    minX = maxX = startX
    minY= maxY = startY
    length = len(grid)
    while minX-1 >= 0 and grid[minX-1][startY] != 'X':
        minX = minX-1
    while maxX+1 < length and grid[maxX+1][startY] != 'X':
        maxX = maxX+1
    while minY-1 >= 0 and grid[startX][minY-1] != 'X':
        minY = minY-1
    while maxY+1 < length and grid[startX][maxY+1] != 'X':
        maxY = maxY+1
    return minX, maxX, minY, maxY
    
def minimumMoves(grid, startX, startY, goalX, goalY):
    boolean_grid = [[True if grid[i][j] == '.' else False for j in range(len(grid[i]))] for i in range(len(grid))] 
    distance_grid = [[0 for j in range(len(grid))] for i in range(len(grid))]
    
    boolean_grid[startX][startY] = False
    queue = [(startX, startY)]
    
    while len(queue) > 0:    
        x, y = queue.pop(0)
        minX, maxX, minY, maxY = find_end(grid, x, y)        
        print(minX, maxX, minY, maxY)
        arr = [(i,y) for i in range(minX, maxX+1)] + [(x,i) for i in range(minY, maxY+1)]
        
        for cor_x, cor_y in arr:
            if cor_x == goalX and cor_y == goalY:
                return distance_grid[x][y]+1
            elif boolean_grid[cor_x][cor_y]:
                boolean_grid[cor_x][cor_y] = False
                distance_grid[cor_x][cor_y] = distance_grid[x][y]+1
                queue.append((cor_x, cor_y))
            
    
        
        
        
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
