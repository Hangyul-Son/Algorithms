
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    count = 0
    
    for i in range(len(q)):
        if q[i] > i + 3:
            return "Too chaotic"
        else:   
            j = i
            while j > 0 and q[j] < q[j-1]:
                q[j], q[j-1] = q[j-1], q[j]
                j -= 1 
                count += 1
                
    return count
            
                
    
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        result = minimumBribes(q)
        fptr.write(str(result)+'\n')
    

    fptr.close()
