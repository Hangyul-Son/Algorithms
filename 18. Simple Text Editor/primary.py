# Enter your code here. Read input from STDIN. Print output to STDOUT

Q = int(input())

stack = []
S = ''
for i in range(Q):
    x = input().rstrip().split()
    command = int(x[0])
    
    if command == 1:
        stack.append(S)
        y = x[1]    
        S = S + y
    elif command == 2:
        stack.append(S)    
        y = x[1]
        S = S[:len(S)-int(y)]
    elif command == 3:
        y = x[1]
        print(S[int(y)-1])
    elif command == 4:
        S = stack.pop()
    