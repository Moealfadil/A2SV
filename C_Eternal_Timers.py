testS=int(input())
for test in range(testS):
    n=int(input())
    nums=list(map(int,input().split()))
    possible=True
    for i in range(n):
        if nums[i] <= 2 * max(i, n-1-i):
            possible=False
            break
    if possible:
        print("YES")
    else:
        print("NO")