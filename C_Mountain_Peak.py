tests=int(input())
for test in range(tests):
    n=int(input())
    h=list(map(int,input().split()))
    # first_low=float("inf")
    # high=0
    # possible=False
    # for i in range(n):
    #     if h[i]<first_low:
    #         first_low=h[i]
    #         high=first_low+1
    #         idx1=i+1
    #         idx2=idx1+1
    #     if h[i]>first_low and h[i]<=high and i>=idx1:
    #         high=h[i]
    #         idx2=i+1
    #     if h[i]<high and i>=idx2:
    #         second_low=h[i]
    #         idx3=i+1
    #         print("YES")
    #         print(*[idx1,idx2,idx3])
    # if not possible:
    #     print("No")
    idx=[0]*n
    for i in range(n):
        idx[h[i]-1]=i
    print(idx)
    