tests= int(input())
for test in range(tests):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    least=float('inf')
    current=0
    for i in range(n-2):
        current= abs(arr[i]-arr[i+1])+abs(arr[i+1]-arr[i+2])
        least=min(least,current)
    print(least)