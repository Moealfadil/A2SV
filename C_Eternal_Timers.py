testS=int(input())
for test in range(testS):
    n=int(input())
    nums=list(map(int,input().split()))
    min_num=min(nums)
    min_index=nums.index(min_num)
    diff= max(abs(min_index-0),abs(min_index-(n-1)))
    if (n==1 and nums[0] >1) or (min_num> 2*diff):
        print("YES")
    else:
        print("NO")