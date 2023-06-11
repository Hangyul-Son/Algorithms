#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Write your code here
    primes =[]
    last = 2
    no_prime = False
    while len(primes) != q:
        for i in range(2, last):
            if last%i==0:
                no_prime = True
                break
        if not no_prime:        
            primes.append(last) 
        no_prime = False
        last += 1
    print(primes)
    
    stack_B = []
    stack_A = []
    result = []
    for i in range(q):
        # while len(number) != 0:
        for j in reversed(number):
            # j = number.pop()
            if j%primes[i]==0:
                stack_B.append(j)
            else:
                stack_A.append(j)        
        # while len(stack_B) != 0:
        # for c in reversed(stack_B):
        result = result + stack_B[::-1]
            # c = stack_B.pop()
            # result.append(c)
        number = stack_A
        stack_A = []
        stack_B = []

        
        
    while len(number) != 0:
        result.append(number.pop())
    return result
    
                
                
                    
          
      
if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    print('\n'.join(map(str, result)))
    print('\n')


    
    
