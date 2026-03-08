n, k=input().split()
n=int(n)
k=int(k)
arr=list(map(int,input().split()))
arr.sort()
possible=arr[k-1]
if k==n:
    print(arr[-1])
elif k==0:
    if arr[0] == 1:
        print(-1)
    else:
        print(arr[0] - 1)
else:
    if possible < arr[k]:
        print(possible)
    else:
        print(-1)