tests=int(input())
for test in range(tests):
    n=int(input())
    nums=list(map(int,input().split()))
    if sum(nums)%len(nums)==0:
        avg=sum(nums)//len(nums)
        count=0
        for num in nums:
            if num>avg:
                count+=1
        print(count)
    else:
        print(-1)