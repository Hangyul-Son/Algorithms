# Enter your code here. Read input from STDIN. Print output to STDOUT

Q = int(input())
A = [0]

def heapify(A):
    index = len(A)-1
    while index > 1 and A[index] < A[index//2]:
        A[index], A[index//2] = A[index//2], A[index]
        index = index//2

def remove_heap(A, val):
    index = A.index(val)
    A[index] = pow(10,9)+1
    while index*2 < len(A):
        if index*2+1 < len(A):
            if A[index*2] <= A[index*2+1]:
                changing_index = index*2
            else:
                changing_index = index*2+1
        else:
            changing_index = index*2
        A[index], A[changing_index] = A[changing_index], A[index]
        index = changing_index
    
for i in range(Q):
    c = list(map(int, input().split()))
    if c[0] == 1:
        A.append(c[1])
        heapify(A)
    elif c[0] == 2:
        remove_heap(A, c[1])
    elif c[0] == 3:
        print(A[1])  
