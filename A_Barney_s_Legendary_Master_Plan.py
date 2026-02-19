tests=int(input())
for test in range (tests):
    n=int(input())
    nums=list(map(int,input().split()))
    print(2*len(set(nums))-1)