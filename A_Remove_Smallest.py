from collections import deque
tests=int(input())
for test in range(tests):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    arr=deque(arr)
    possible=True
    while len(arr)>1:
        if abs(arr[1]-arr[0])<=1:
            arr.popleft()
        else:
            possible=False
            break
    if possible:
        print("YES")
    else:
        print("NO")
        